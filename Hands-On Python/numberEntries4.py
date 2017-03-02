
def numberList(items):
    '''Print each item in a list items, numbered in order.'''
    number = 1
    for item in items:
        print number, item
        number = number + 1
        
def main():
    numberList(['red', 'orange', 'yellow', 'green'])
    print
    numberList(['apples', 'pears', 'bananas'])
        
main()

def sumList(nums):
    '''Return the sum of the numbers in nums.'''
    total = 0
    for num in nums:
        total = total + num
        return total
        
print sumList([1, 2, 3, 4])