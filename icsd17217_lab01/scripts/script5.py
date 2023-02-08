import os
import sys
import subprocess
import re
os.system("sudo grep -Po '^[^:]*(?=::)' /etc/shadow > noPass")
with open('noPass') as file:
	for line in file:
		user = line.strip()
		print(user)
		try:
			output = subprocess.run(['userdel',user])
			if output.returncode == 0:
				print("User ",user," was deleted")
		except:
			print("Failed to delete")
			
