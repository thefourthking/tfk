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



f = open('/opt/fourthking/student_list', 'r')

function.log("Running cron job")
for line in f:

	# pulling data from the student_list file for getting the list of users who have submitted assignments
	print line

	data = line.strip('\n')
	data = data.split(',', 3 )
	
	userid =  data[0]
	username = data[1]
	labid = data[2]
	language = data[3]

	

	filedir = "/home/" + username
	filename = username + "_" + labid + "." + language

	# look for the code file of the assignment in the directory specified to the user.
	# the specified folder being the home folder of the user. i.e. /home/<username>/<user_id>_<lab_id>.java
	code_found = 0
	print "Looking for " + filename + " in " + filedir
	for file in os.listdir( filedir ):
		code_found = 0
		if fnmatch.fnmatch(file, filename):	
			code_found = 1


		if code_found == 1:
		# create the results.json if non-existent

			resultfolder = "/opt/fourthking/results/" + userid 
			if(os.path.isdir(resultfolder) == 1):
				print "Folder exists"
			else:
				os.makedirs(resultfolder)

			print "Evaluating assignment and grading"
			# call the code that will evaluate and grade the assignment

			json_content= {}
			json_content['student_id'] = userid
			json_content['lab_id'] = labid
			json_content['score'] = int(userid)*100

			resultfile = resultfolder + "/result_" + labid + ".json"
			resultjson = open(resultfile, "w")
			resultjson.write(json.dumps(json_content))
	





