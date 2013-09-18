import urllib
import urllib2

url = 'http://localhost:8080/createJSON.py'
values = {
			'username' : 'prateek',
          	'labid' : '1' 
         }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()