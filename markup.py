# coding=utf-8
import  re

from util import *
from rules import *


# from handers import *
# import sys

class Parser:
"""
语法分析器读取文本文件、应用规则并且控制处理程序。
"""
    def  __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):         # re模块sub函数的应用：模板-函数替换
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        blocks = Block(file)
        for block in blocks:
            for filtter in self.filters:
                block = filtter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')

class BasicTextParse(Parser):
"""
在构造函数中增加规则和过滤器的具体语法分析器
"""
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())        # 这里解析的顺序不能随意变换
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

