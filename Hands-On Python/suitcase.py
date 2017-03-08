# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 08:49:41 2017

@author: tim.latham
"""

weight = input('How many pounds does your suitcase weigh? ')
if weight > 50:
    print 'There is a $25 charge for luggage that heavy.'
print 'Thank you for your business'

temperature = input('What is the temperature? ')
if temperature > 70:
    print 'Wear shorts.'
else:
    print 'Wear long pants.'
print 'Get some exercise outside'

credit = input('How many credits do you have? ')
if credit >= 128:
    print 'Congratulations, you are ready to graduate!'
else:
    print '128 credits are required to graduate, keep working!'
print 'School is fun!'

def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime at 1.5 times for
    hours over 40.
    '''
    if totalHours > 40.0:
        weeklyWages = (40.0 * hourlyWage) + ((totalHours - 40.0) * (hourlyWage * 1.5))
    else:
        weeklyWages = totalHours * hourlyWage
    return float(weeklyWages)

def main():
    hours = input('Enter hours worked: ')
    wage = input('Enter dollars paid per hour: ')
    total = calcWeeklyWages(hours, wage)
    print 'Wages are $%.2f.' % total
    
main()
