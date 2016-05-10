#! /usr/bin/python

import subprocess

output = subprocess.check_output("./getHosts.sh", shell=True)

i=9001
print "#ip,port"
for line in output.split():
	print line + "," + str(i)
	i += 1
