# Python script to be executed after the student submits an assignment
# this script generates the result in the /opt/fourthking/results/<userid>/<labid>/result.json
#
# command format:
# createJSON 

import fnmatch
import sys
import os
import json
import function
import subprocess



f = open('/opt/fourthking/student_list', 'r')

function.log("Running cron job")
for line in f:

	# pulling data from the student_list file for getting the list of users who have submitted assignments
	data = line.strip('\n')
	data = data.split(',', 3 )
	
	userid =  data[0]
	username = data[1]
	labid = data[2]
	language = data[3]

	

	filedir = "/home/" + username
	filename = "lab_" + labid + "." + language
	#filename = username + "_" + labid + "." + language

	# look for the code file of the assignment in the directory specified to the user.
	# the specified folder being the home folder of the user. i.e. /home/<username>/lab_<lab_id>.java
	code_found = 0
	for file in os.listdir( filedir ):
		code_found = 0
		if fnmatch.fnmatch(file, filename):	
			code_found = 1

		if code_found == 1:
		# create the results.json if non-existent

			resultfolder = "/opt/fourthking/students/" + userid 
			if(os.path.isdir(resultfolder) != 1):
				function.log("Creating student_id folder")
				os.makedirs(resultfolder)
				os.makedirs(resultfolder+"/results");

			function.log( "Evaluating assignment and grading")

			#--------------------------------------------------------------
			# call the code that will evaluate and grade the assignment
		        copy_code="cp " + filedir +"/lab_" + labid + ".java /opt/fourthking/unit_tests/"	
			prep_junit="cd /opt/fourthking/unit_tests" + \
			";javac -cp '/opt/fourthking/lib/junit-4.7.jar:.' lab_" + labid + "Test.java;" + \
			"junit lab_" + labid + "Test | grep 'Tests run' | awk '{print $3}' | awk -F',' '{print $1}'" 
			f = os.popen(copy_code)
			
			f = os.popen(prep_junit)
			total_tests=f.read()
			total_tests=int(total_tests)
			
			prep_junit="cd /opt/fourthking/unit_tests" + \
			";junit lab_" + labid + "Test | grep 'Tests run' | awk '{print $5}' | awk -F',' '{print $1}'" 
			f = os.popen(prep_junit)
			failed_tests=f.read()
			failed_tests=int(failed_tests)
			
			passed_tests=total_tests-failed_tests
			#--------------------------------------------------------------
			
			json_content= {}
			json_content['student_id'] = userid
			json_content['lab_id'] = labid
			json_content['score'] = passed_tests
			json_content['total_tests'] = total_tests
			json_content['failed_tests'] = failed_tests
			
			#writing the json to the file
			resultfile = resultfolder + "/results/"  + labid + ".json"
			resultjson = open(resultfile, "w")
			resultjson.write(json.dumps(json_content))
	

			cleanup="cd /opt/fourthking/unit_tests"  ";rm *.class;ls -1 | grep -v 'Test' | xargs rm -f" 
			f = os.popen(cleanup)




