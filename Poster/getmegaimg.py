from xml.etree.ElementTree import *
import re
#print('\rOPEN: 20 %')
file = open('data.txt').read()
#i = 0
while file.find('\n\n') != -1:
#    print('\rOPEN:', i+40, '%', '( DAT =', repr(file[file.find('\n\n')-10:file.find('\n\n')+10]), ')')
    file = file.replace('\n\n', '\n')
#    i+=1
#print('\rOPEN: 60 %')
#file = re.sub(r'<([a-zA-Z])([^/\n]*)>', r'<\1\2/>', file)
#print('\rOPEN: 80 %')
#file = file.replace('</span/>', '</span>')
#print('\rOPEN: 100 %')
try:
    for element in XML(file).findall('.'):
        print(element.attrib['class'])
except ParseError as err:
    data = ()
    if err.msg.startswith('mismatched tag'):
        data = (int(err.msg[21:err.msg.find(',', 22)]), int(err.msg[-2:]))
    print(data)
