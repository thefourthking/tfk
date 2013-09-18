# Python script to be executed after the student submits an assignment
# this script generates the result in the /opt/fourthking/results/<userid>/<labid>/result.json
#
# command format:
# createJSON 

import fnmatch
import sys
import os


f = open('/opt/fourthking/student_list', 'r')

for line in f:

	# pulling data from the student_list file for getting the list of users who have submitted assignments
	print line

	data = line.strip('\n')
	data = data.split(',', 1 )
	
	username =  data[0]
	labid = data[1]


	#get username using user id from the DB
	username = "prateek" # temporary hard coded value
	language = "java"
	# codeto be written here


	filedir = "/home/" + username
	filename = username + "_" + labid + "." + language

	# look for the code file of the assignment in the directory specified to the user.
	# the specified folder being the home folder of the user. i.e. /home/<username>/<user_id>_<lab_id>.java
	code_found = 0
	print "Looking for " + filename + " in " + filedir
	for file in os.listdir( filedir ):
		if fnmatch.fnmatch(file, filename):	
			code_found = 1
			print "Evaluating assignment and grading"
			# call the code that will evaluate and grade the assignment

	if code_found == 1:
		# create the results.json if non-existent
		resultjson = open("/opt/fourthking/results/1/result.json", "w")
		resultjson.write("JSON contents")
	


