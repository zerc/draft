#!/usr/bin/env python
#-*- coding:utf-8 -*-

from string import count

l = (
'cat',
'cat/sub1',
'cat/sub2',
'cat/sub3/subsub1',
'cat/sub3/subsub2',
'cat/sub4',
'cat1',
'cat1/sub1_1',
'cat1/sub1_2',
)

indexs = [0]

for x in l:
    level = x.count('/') 
    if level == 0:
        indexs[level] += 1
        del indexs[1:]
        print x, ' -- ',indexs[level]
    elif level > 0:
        try: indexs[level] += 1
        except: indexs.insert(level, 1)
        print x, ' ++ ',indexs[level]
   
