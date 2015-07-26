#!/usr/bin/python
## 
## dynamic.py

def load_class(cl):
    d = cl.rfind(".")
    classname = cl[d + 1:len(cl)]
    classname = classname.encode('ascii', 'ignore')
    m = __import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)


def call_method(obj, method, args):
    return getattr(obj, method)(*args)


def test_import():
    print("Dynamic Imported")
