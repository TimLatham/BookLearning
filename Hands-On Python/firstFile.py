# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 15:42:17 2017

@author: tim.latham
"""

outFile = file('sample.txt', 'w') # the w parameter indicates you're going to write to the file specified
outFile.write('My first output file!')
outFile.close() # It is critical to close the file at the end to ensure it gets written to

outFile2 = file('sample3.txt', 'w')
outFile2.write('A revised revised output file!\n')
outFile2.write('Write some more.\n')
outFile2.close()

inFile = file('sample3.txt', 'r') #the r parameter is also the default, tells it you're going to read
contents = inFile.read() # using the close method is generally optional with files being read
print contents