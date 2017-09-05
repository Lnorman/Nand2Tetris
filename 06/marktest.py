# File test.py

lines = open(__file__).readlines()
print 'lines =', lines

print

lines = []
for line in open(__file__):
   lines += [line]
print 'lines =', lines
