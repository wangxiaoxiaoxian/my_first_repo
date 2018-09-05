#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 19:43
# @Author  : Smart Porridge
# @File    : main.py
# @Software: PyCharm Community Edition
# @Dsc     : main
import os
file1=open('./test.txt','w')
list1=os.listdir('./')
print(list1)
for i in list1:
    print(i)
    file1.write(i)
    file1.write('\n')

file1.close()

print '........'
file2=open('./test.txt')
lines=file2.readlines()
for line in lines:
    print(line)