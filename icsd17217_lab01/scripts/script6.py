import datetime
import re
import subprocess
import os
import sys
searchfor = sys.argv[1]


str1 = "sudo cat /home/*/"+searchfor+"/.bash_history > historySearch2"
str2 = "sudo cat /home/"+searchfor+"/.bash_history >> historySearch2"


os.system(str1)
os.system(str2)
with open('historySearch2') as f:
        lines = f.readlines()
length = len(lines)
for i in range(length):
        result = re.search('[a-zA-Z]',lines[i])
        commnd = lines[i].rpartition(':')[2].strip()
        if result != None:
                i = i - 1;
                epochcode = lines[i].rpartition('#')[2]
                date = datetime.datetime.fromtimestamp(int(epochcode))
                print(date," ",commnd)
