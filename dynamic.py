#!/usr/bin/python
## 
## dynamic.py

def loadClass(cl):
    d = cl.rfind(".")
    classname = cl[d+1:len(cl)]
    m = __import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)

def callMethod(obj,method,args):
	return getattr(obj, method)(*args)

def testImport():
	print "Dynamic Imported"