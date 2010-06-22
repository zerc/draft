#!/usr/bin/env python
#-*- coding:utf-8 -*-
# zerc.ru
# Библиотека базовых функиций

import os

def get_(path, name, exc=[]):
# Возвращает список файлов или директорий, лежащих в path
# и удовлетворяющих условию name и не лежащие в папках из списка exc
# name может быть:
# - filename.xxx - полное имя файла
# - .xxx - только расширение
# - dirname - название папки
	result = []
    	for root, dirs, files in os.walk(path):
    		if "." not in name and len(dirs):
    		# Дано название директории
    			result += [os.path.join(root,x) for x in dirs if x == name]
    		elif len(files):
    			if name[0] == ".":
    				result += [os.path.join(root,x) for x in files if x[-len(name):] == name]
    			elif name[-1] == ".":
    				result += [os.path.join(root,x) for x in files if x[:len(name)] == name]
    			else:
    				result += [os.path.join(root,x) for x in files if name == x]

	return [x for x in result if len([y for y in exc if y in x]) == 0]	

def openfile(path, mode='r', t='list'):
# Открывает файл path, в режиме mode, если mode==w то возврщает объект файл
# t (type) - если режим чтения, то этот параметр определяет в каком виде возврщать файл
# str- строка, list - список
	f = open(path, mode)
	if mode == 'w':
		return f
	elif mode == 'r':
		if t == 'list':
			a = f.readlines()
			f.close()
			return a
		elif t == 'str':
			a = f.read()
			f.close()
			return a
	return None
			
			
#a = get_('/home/zero13cool/www/django', 'models.py')
#f = openfile(a[0],t='str')
#print f
