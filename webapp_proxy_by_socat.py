#!/usr/bin/python
import urllib2

# HOW TO RUN with socat
#  $ chmod +x webapp_proxy_by_socat.py
#  $ socat TCP4-listen:1337,reuseaddr,fork EXEC:./webapp_proxy_by_socat.py
#
#  Meaning:
#	- Listen at Port 1337/tcp
#	- allows reusing of address
#	- can create forks (child for multi-threading)
#	- executes python script
#  Note: man socat for more info (PS. requires installation of socat)
#########################

# open random socket to connect to web server (random, everytime you run this program)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_method = ""
data = ""
data_field = ""
user_input = ""
filtered_user_input = ""
input = ""
while(1):
	#print "test test"
	# assume that this is a web application proxy
	# get user input
	# remember '\r\n\r\n'
	
	user_input = raw_input()
	
	
	filtered_user_input = user_input #no filtering yet
	
	
	fields = filtered_user_input.split('\r\n')
	http_method = fields[0]
	http_method_split = http_method.split(' ')
	if(http_method_split[0] == 'GET'):
		req = urllib2.Request('http://10.0.2.15'+http_method_split[1])
	elif(http_method_split[0] == 'POST'):
		req = urllib2.Request('http://10.0.2.15')
	# obtain request via raw request
	fields_without_method = fields[1:] #everything except first field
	if(http_method_split[0] == 'POST'):
		data_field = fields[len(fields)-3] #only last field
	output = {}
	for field in fields_without_method:
		if(field == '' or ':' not in field):
			break
		key, value = field.split(':')
		req.add_header(key, value)
		
	if(http_method_split[0] == 'POST'):
		req.add_data(data_field)


	# send it to 10.0.2.15:80
	c_recv = urllib2.urlopen(req)
	# wait for webserver to reply
	data = c_recv.read()
	print data
	# loop until connection is terminated
	
	
	
	#print "end test"
