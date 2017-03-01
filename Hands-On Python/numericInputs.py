# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 12:16:50 2017

@author: tim.latham
"""

'''Two numeric inputs'''

'''
The prompt works the same way as with raw_input. This 
version is much more powerful than the version with the 
int conversion of strings. As in the shell, arbitrary 
expressions in the input are evaluated: 
As a test, run the program entering the expressions 5-1 and 2*3.
'''

x = input("Enter a number: ")
y = input("Enter a second number: ")
print 'The sum of %s and %s is %s.' % (x, y, x+y)