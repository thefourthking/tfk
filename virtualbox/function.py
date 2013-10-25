def log(x):
	from time import strftime,localtime
	f = open('/opt/fourthking/log', 'a+')
	timestamp = strftime("%Y:%m:%d:%H:%M:%S: ",localtime())
	f.write(timestamp  + x +"\n")




