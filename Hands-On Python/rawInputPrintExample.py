# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 11:21:32 2017

@author: tim.latham
"""

'''Illustrate raw_input and print.'''

applicant = raw_input("Enter the applicant's name: ")
interviewer = raw_input("Enter the interviewer's name: ")
time = raw_input("Enter the appointment time: ")
print interviewer, "will interview", applicant, "at", time
print '%s will interview %s at %s.' % (interviewer, applicant, time)