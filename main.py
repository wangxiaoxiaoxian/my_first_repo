#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 19:43
# @Author  : Smart Porridge
# @File    : main.py
# @Software: PyCharm Community Edition
# @Dsc     : main
import os
import time
file1=open('./test.txt','w')
list1=os.listdir('./')
print(list1)
for i in list1:
    ticks=time.asctime(time.localtime(time.time()))
    print"当前时间为:",ticks
    print(i)
    file1.write(i)
    file1.write('\n')
    file1.write(str(ticks))
    file1.write('\n')


file1.close()

print '........'
file2=open('./test.txt')
lines=file2.readlines()
length=len(lines)
print('this file has:',str(length))
for line in lines:
    print(line)
