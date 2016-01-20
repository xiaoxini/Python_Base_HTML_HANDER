# coding=utf-8
import re

from util import *

f = open('test02.html', 'w+')
f.write("<html><head><title>...</title><body>")

title = True
for block in Block(open('test01.txt')):
    block = re.sub(r'\*([.+?])\*', r'<em>\1</em>', block)
    if title:
        f.write('<h1>')
        f.writelines(block)
        f.write('</h1>')
        title = False
    else:
        f.write('<p>')
        f.writelines(block)
        f.write('</p>')
f.write('</body></html>')
f.close()







