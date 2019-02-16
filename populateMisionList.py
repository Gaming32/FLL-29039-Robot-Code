import re
import zipfile
import sys

class display:
    def __init__(self, filename):
        self.file = open(filename, 'w')
    def write(self, text):
        sys.stdout.write(text)
        self.file.write(text)
file = display('MissionList.txt')
for program in zipfile.ZipFile('ORBIT3R-BOT.ev3').namelist():
    if re.search(r'M[0-9][0-9]_.*\.ev3p\.mbxml', program) != None:
        print(program.replace('.ev3p.mbxml',''), file=file)
print('001', file=file)