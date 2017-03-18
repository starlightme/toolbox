#!/usr/bin/env python
# -*- coding:utf-8 -*-

# mainly for sql query

filename = 'test.txt'

with open(filename,'r') as fp:
    l = fp.readlines()

l = map(  lambda s:s.strip(), l )

result = str(l).replace('[','(').replace(']',')')

print result

with open(filename,'a') as fp:
    fp.write(result)