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
z, a = input("Enter two comma separated numbers: ")
b, c, d = input("Enter three comma separated numbers: ")

print 'The sum of %s and %s is %s.' % (x, y, x+y)
print 'The sum of %s and %s is %s.' % (z, a, z+a)
print 'The sum of %s and %s and %s is %s.' % (b, c, d, b+c+d)

e, f = input("Enter two comma separated numbers, the first to be divided by the second: ")
print 'The quotient of %s and %s is %s with a remainder of %s' % (e, f, e/f, e%f)
quotient = e/f
remainder = e%f
print 'The quotient of %s and %s is %s with a remainder of %s' % (e, f, quotient, remainder)