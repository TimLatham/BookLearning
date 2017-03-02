"""A tiny English to Spanish dictionary is created,
using the Python dictionary type dict.
Then the dictionary is used, briefly.
"""

# Exercise 1
spanish1 = {}
spanish1['hello'] = 'hola'
spanish1['yes'] = 'si'
spanish1['one'] = 'uno'
spanish1['two'] = 'dos'
spanish1['three'] = 'tres'
spanish1['red'] = 'rojo'
spanish1['black'] = 'negro'
spanish1['green'] = 'verde'
spanish1['blue'] = 'azul'

print spanish1['two']
print spanish1['red']
print spanish1

# Exercise 2
def createDictionary1():
    '''Returns a tiny Spanish dictionary'''
    spanish = {}
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    return spanish
    
def main():
    dictionary = createDictionary1()
    print dictionary['two']
    print dictionary['red']

main()

# Exercise 3
numDict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print numDict['two']
print numDict['four']
print "Count in numerals: %(one)s, %(two)s, %(three)s, %(four)s, ..." % numDict

# Exercise 4
def createDictionary():
    '''Returns a tiny Spanish dictionary'''
    spanish = {}
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    return spanish
    
def main():
    dictionary = createDictionary()
    print "Count in Spanish: %(one)s, %(two)s, %(three)s, ..." % dictionary
    print "Spanish colors: %(red)s, %(blue)s, %(green)s, ..." % dictionary

main()
