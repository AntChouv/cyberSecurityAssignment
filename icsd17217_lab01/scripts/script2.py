import datetime
import re
import subprocess
import os
import sys
searchfor = sys.argv[1]


str1 = "sudo grep -B1 -e "+searchfor+" /home/*/.bash_history > historySearch"
str2 = "sudo grep -B1 -e "+searchfor+" /home/*/*/.bash_history >> historySearch"

os.system(str1)
os.system(str2)

with open('historySearch') as f:
	lines = f.readlines()
length = len(lines)
for i in range(length):
	result = re.search('/home/(.*)/.bash_history:',lines[i])
	commnd = lines[i].split(':',1)[-1]
	commnd.split()
	if result != None:
		i = i - 1;
		epochcode = lines[i].rpartition('#')[2]
		date = datetime.datetime.fromtimestamp(int(epochcode))
		print(result.group(1)," ",date," ",commnd)
	#if result1 != None:
		#print(result1.group(1))
