#!/usr/bin/python
# -*- coding:utf-8 -*-
# 将markdown文档转化为html文档
# 说明：需要pip安装markdown和pygments

import sys
import os

file_name = ''.join(sys.argv[1:])
print file_name

# os.system会打开一个命令窗口和阻塞程序继续运行
# os.popen('').read()不显示窗口，若取消阻塞则去掉read()
# os.startfile和subprocess.Popen能够不阻塞
os.popen('markdown_py -x codehilite '+file_name+' > output.html').read()

with open('output.html', 'r') as f:
	r_content = f.read()

os.popen('rm output.html').read()

with open(file_name[:-3]+'.html', 'w') as f:
	text_before = '''
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
	<link rel="stylesheet" type="text/css" href="code.css">
</head>
<body>
	'''
	text_after = '''
</body>
</html>
	'''
	f.write(text_before)
	f.write(r_content)
	f.write(text_after)

# 判断code.css存在与否，不在就要创建一个
r_css = [i for i in os.popen('ls code.css').read().split('\n') if i]
if not r_css:
	os.popen('pygmentize -S default -f html -a .codehilite > code.css')











