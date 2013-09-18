import sys
import urllib2
if len(sys.argv) != 3:
	print "Invalid number of arguments"
else:
	print "The userid called is:",sys.argv[1]
	print "The lab requested is:",sys.argv[2]
	
	print "Here is the JSON file"
	response = urllib2.urlopen('http://localhost:8000/results/1/result.json')
	html = response.read()
	print html
