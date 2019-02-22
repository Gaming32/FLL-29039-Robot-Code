import sys
from zipfile import *
z = ZipFile(sys.argv[1])
zw = []
end = sys.argv[4] if len(sys.argv)>4 else ''
for f in (f for f in z.namelist() if f.endswith(end)):
	print(f)
	#.lower().find(sys.argv[2].encode())
	#for match in z.open(f).read().lower().find(sys.argv[2].encode()):
	#	print(bytes([match]).decode(), end='')
	b = z.read(f).lower().decode()
	#print(b)
	b = b.replace(sys.argv[2], sys.argv[3])
	zw.append((f, b))
z.close()
z = ZipFile(sys.argv[1], 'w')
for (f, b) in zw:
	z.writestr(f, b)