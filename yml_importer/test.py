#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulStoneSoup

xml = """
<root>
	<cat id="1">cat1</cat>
	<cat id="2" parent="1">subcat1</cat>
	<cat id="3" parent="2">subcat2</cat>
	<cat id="4" parent="2">subcat3</cat>
	<cat id="5">cat2</cat>
	<cat id="6" parent="5">subcat1</cat>
</root>"""

soup = BeautifulStoneSoup(open('test.xml','r').read())

def get_parents(soup, item):
	""" возвращает последовательность категория-подкатегория-подкатегория и тд"""
	path = [item.string]
	i=1
	for x in soup.findAll({'category':True}):
		#print x.attrs
		#if len(x.attrs)==1 and x.attrs[0][1] == item.attrs[1][1]:
		#print x.string
		#print x.attrs
		#print item.string
		#print item.attrs, '--', len(item.attrs)
		#print '========'
		if len(x.attrs) == 1:
			path.append(x.string)
			#print x.string
		elif len(x.attrs)==2 and len(item.attrs) == 2:
			if x.attrs[1][1] == item.attrs[1][1] or x.attrs[0][1] == item.attrs[1][1]:
				path.append(x.string)
		elif len(x.attrs)==2 and len(item.attrs) == 1 and x.attrs[1][1] == item.attrs[0][1] :
			path.append(x.string)
			#print x.string
		i+=1
		#if len(x) == 2:
		#	pass
	#print x.attrs, x.string
	path = path[1:]
	#path.reverse()
	return '/'.join(path)
	

for x in soup.findAll({'category':True}):
	print get_parents(soup, x)