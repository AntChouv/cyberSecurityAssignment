import os
import subprocess
import getpass
import re
import sys
import crypt
def addNewUser():
	username = input("Enter the username : ")
	flag = 1
	while (flag == 1):
		password = getpass.getpass()
		flag = 0
		while True:
			if (len(password)<6):
				print("Needs to be 8 chars")
				flag = 1
				break
			elif not re.search("[a-z]", password):
				print("Needs to have a lowercase letter")
				flag = 1
				break
			elif not re.search("[A-Z]", password):
				print("Needs to have an upercase letter")
				flag = 1
				break
			elif not re.search("[0-9]", password):
				print("Needs to have a number")
				flag = 1
				break
			elif not re.search("[_@$]", password):
				print("Needs to have a special char")
				flag = 1
				break
			elif re.search("\s", password):
				flag = 1
				break
			else:
				print("Valid Password")
				break
		passwordconf = getpass.getpass("Retype password : ")
		if (password != passwordconf):
			print("Passwords do not match")
			flag = 1


	try:
		encrytPass = crypt.crypt(password)
		subprocess.run(['useradd','-p',encrytPass,username])
		group = input("Enter your groups name : ")
		parent_dir = "/home/"
		bsh_files = "/etc/skel/."
		hist = ".bash_profile"
		subprocess.run(['adduser',username,group])
		subprocess.run(['usermod',username,'--shell','/bin/bash'])
		mode = 0o704
		path = os.path.join(parent_dir,group,username)
		path2 = os.path.join(path,hist)
		path3 = os.path.join(path,bsh_files)
		os.mkdir(path,mode)
		subprocess.run(['cp','-a',bsh_files,path])
		subprocess.run(['usermod','-m','-d',path,username])
		subprocess.run(['chown',username,path])
	except:
 		print("failed to add user.")
	sys.exit(1)
addNewUser()


