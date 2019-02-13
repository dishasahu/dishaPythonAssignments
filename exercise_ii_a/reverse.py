# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:41:01 2019

@author: abc
"""

num=int(input("enter the number"))
a=int(num%10+1)
rev=rev*10+a
num=num/10

b=int(num%10+1)
rev=rev*10+a
num=num/10

c=int(num%10+1)
rev=rev*10+a
num=num/10

d=int(num%10+1)
rev=rev*10+a
num=num/10

e=int(num%10+1)
rev=rev*10+a
num=num/10

print(rev)