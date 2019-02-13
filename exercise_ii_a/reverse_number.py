# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:41:01 2019

@author: abc
"""

num=int(input("enter the number"))
a=int(num%10)
rev=a
num=num/10

a=int(num%10)
rev=rev*10+a
num=num/10

a=int(num%10)
rev=rev*10+a
num=num/10

a=int(num%10)
rev=rev*10+a
num=num/10

a=int(num%10)
rev=rev*10+a
num=num/10

print(rev)