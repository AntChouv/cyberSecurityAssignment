import os
import sys
import subprocess
import re
newNumber = sys.argv[1]
searchFor = ' '
with open('/etc/pam.d/common-auth','r') as file:
	for line in file:
		for word in line.split():
			if word.startswith("deny"):
				searchFor = word
				break

line = "2s/"


end = "/"
combined =line + searchFor + end + newNumber + end



subprocess.run(["sudo","sed","-i",combined,"/etc/pam.d/common-auth"])
#os.system('cat /etc/pam.d/common-auth | grep -o \'deny=[^ ,]\+\''

#os.system('sudo sed -i "2s/deny=4/deny=2/" /etc/pam.d/common-auth')
