# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:43:39 2017

@author: tim.latham
"""

def acronym_me():
    sentence = raw_input("Enter the words you'd like to acronym: ")
    sentence_list = sentence.split()
    acronym = ''
    for word in sentence_list:
        if word[0].isalpha():
            acronym = acronym + word[0].upper()
    return acronym

print acronym_me()