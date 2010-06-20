#!/usr/bin/python
#-*- coding:utf-8 -*-
# zerc.ru

from os import popen


def get_free():
	s = tuple(popen('free -m').readlines()[1].split()[1:4])
	return s
	
def index():
	html = """
<html>
<head><title>web free</title></head>
<body>
<style type="text/css">
body {margin:0;padding:0;background:#aeaeae;color:#ffffff;}
.main {width:300px;margin:0 auto 0 auto;text-align:center;}
.main table {border:1px solid #444444;}
.main table td {padding:5px;width:100px;text-align:center;}
.main table .title {background-color:#cccccc;color:#000000;font-weight:bolder;}
.main h3 {text-transform:uppercase;font-size:16px;margin:5px 0 5px 0;}
.main .copy {width:300px;text-align:right;margin:5px 0 5px 0;}
</style>
<div class="main">
	<h3>Использование оперативки</h3>
	<table border="1" cellpadding="0" cellspacing="0" >
	<tr class="title">
		<td>Всего</td>
		<td>Занято</td>
		<td>Свободно</td>
	</tr>
	<tr>
		<td>%s, Мб</td>
		<td>%s, Мб</td>
		<td>%s, Мб</td>
	</tr>
	</table>
	<div class="copy"><b>webFree</b> &copy; zerc</div>
</div>
</body>
</html>"""  % get_free()
	return html