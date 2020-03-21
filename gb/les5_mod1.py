import os
import sys

name = 'dir'
for i in range(1,10):
	newD = os.path.join(os.getcwd(),'{}_{}'.format(name,i))
	os.mkdir(newD)
	print("I made folder, named %s" % newD)
