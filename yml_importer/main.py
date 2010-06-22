#!/usr/bin/python
# -*- coding: utf-8 -*-
# Разбор xml файла ozon'a
# Автор: http://zerc.ru

from BeautifulSoup import BeautifulStoneSoup
from template import csv
from functions import functions as func
from string import count, replace

soup = BeautifulStoneSoup(open('test_back.xml').read())

category_list = soup.findAll('category')
category_list.reverse()

done = [] 

def make_three(category_list, x, root):
	""" возвращает структуру потомок/родитель/родитель и тд бесконечной вложенностью """
	s = [x.string.replace("/","-")]
	for y in category_list:
		if len(x.attrs) == 2:
			if x.attrs[1][1] == y.attrs[0][1]:
				s.append(y.string.replace("/","-"))
				x = y
		elif len(x.attrs) == 1:
			s.append(y.string.replace("/","-"))
			break
	s.reverse()
	print '/'.join(s)
	return '/'.join(s)
	
	
buffer = []
for x in category_list:
	#if category_list.index(x) == 30:
	#	break
	# Перебор списка категорий
	if len(x.attrs) == 2: 
		buffer.append(x)
		#print x.string, " sdsa"
	elif len(x.attrs) == 1:
		buffer.append(x)
		for y in buffer:
			#buffer.reverse()
			#for z in buffer:
			#	print z.string
			#break
			#buffer.reverse()
			done.append(make_three(buffer, y, x.string))
		buffer = []
			#break
		done[-1] = x.string


done.reverse()

to_w = [csv.header]

indexs = [0]
i = 0
for x in done:
	#if done.index(x) == 30:
	#	break
	level = x.count('/') 
	if level == 0:
		indexs[level] += 1
		del indexs[1:]
		to_w.append(csv.row % (x, indexs[level]))
		#print x, ' -- ',
	elif level > 0:
		try: 
			indexs[level] += 1
			to_w.append(csv.row % (x, indexs[level]))
			if i < len(done) and done[i+1].count('/') < level:
				del indexs[level]
		except: 
			if i != len(done)-1: # удаление дубля, если последний элемент был удален
				indexs.insert(level, 1)
				to_w.append(csv.row % (x, indexs[level]))
	i += 1
	
f = func.openfile('new.csv', 'w')
f.write('\n'.join(to_w).encode('utf-8'))
f.close()
print "done"








