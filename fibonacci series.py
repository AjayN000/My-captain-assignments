# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:55:04 2022

@author: Ajay Vignesh
"""

def fib(n):
    if (n == 0):
            return 0
    elif (n == 1):
            return 1
    else :
            return (fib(n-2)+fib(n-1))
n = int(input("Enter the Range Number:"))
for n in range(0,n):
    print(fib(n))
    
    