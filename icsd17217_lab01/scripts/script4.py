import subprocess
import sys
import os
hostname = subprocess.run("hostname")
print()
#subprocess.run('cat','/etc/os-realease')
with open('/etc/os-release','r') as file:
	for line in file:
		print(line)

subprocess.run("uptime")
print()
subprocess.run("who")


