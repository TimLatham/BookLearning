# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 15:08:37 2017

@author: tim.latham
"""

story = """
Once upon a time, deep in an ancient jungle,
there lived a %(animal)s.  This %(animal)s
liked to eat %(food)s, but the jungle had
very little %(food)s to offer.  One day, an
explorer found the %(animal)s and discovered
it liked %(food)s. The explorer took the 
%(animal)s back to %(city)s, where it could
eat as much %(food)s as it wanted. However,
the %(animal)s became homesick, so the 
explorer brought it back to the jungle,
leaving a large supply of %(food)s.

The End
"""


def addCategories(story):
    startPos = 0
    categoryList = []
    while story.find('%', startPos) > -1:
        wordStart = story.find('%', startPos) + 2
        wordEnd = story.find(')', startPos)
        word = story[wordStart:wordEnd]
        if word not in categoryList:
            categoryList.append(word)
        startPos = wordEnd + 1
    return categoryList

print addCategories(story)