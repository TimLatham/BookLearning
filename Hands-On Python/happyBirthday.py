# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 16:10:44 2017

@author: tim.latham
"""

def happyBirthdayEmily():
    print "Happy Birthday to you!"
    print "Happy Birthday to you!"
    print "Happy Birthday dear Emily."
    print "Happy Birthday to you!"
    
def happyBirthdayAndre():
    print "Happy Birthday to you!"
    print "Happy Birthday to you!"
    print "Happy Birthday dear Andre."
    print "Happy Birthday to you!"
    
def main():    
    happyBirthdayEmily()
    happyBirthdayAndre()
    
main()

def happyBirthday(name):
    for i in range (2):
        print "Happy Birthday to you!"
    print "Happy Birthday dear %s." % name
    print "Happy Birthday to you!"
    
def main2():
    happyBirthday('Emily')
    happyBirthday('Andre')
    
main2()

def happyBirthdayInput(person):
    for i in range (2):
        print "Happy Birthday to you!"
    print "Happy Birthday dear %s." % person
    print "Happy Birthday to you!"
    
def main3():
    userName = raw_input("Enter the Birthday person's name: ")
    happyBirthdayInput(userName)
    
main3()