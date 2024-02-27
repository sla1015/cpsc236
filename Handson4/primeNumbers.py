# -*- coding: utf-8 -*-
"""
Prime Number Functions
"""


#prime number main
#     cont = 'y'
#     while cont.lower() == 'y':
#         num = int(input("Please enter an integer between 1 and 5000: "))
#         validateInput(num)
#         factors = calcFactors(num)
#         if factors == 2:
#             print(num, " is a prime number.")
#         else:
#             print(num, " is NOT a prime number. \nIt has", factors, "factors.")
#         cont = input("Try again? (y/n): ")  
#     print("Okay, bye!")


def validateInput(num):
    '''ensures a valid integer is entered'''
    while num <=1 or num >= 5000:
        print("Invalid integer. Please try again.")
        num = int(input("Please enter an integer between 1 and 5000: "))
    return num
        


def calcFactors(x, factors):
    '''determines how many factors argument x has and returns that number'''
    numFactors = 0
    
    for i in range(1, x+1):
        if x % i == 0:
           numFactors += 1 
           factors.append(i)
    return numFactors


def main():
    factors = []
    x = int(input("Enter an integer: "))
    calcFactors(x, factors)
    print(x)
    print(factors)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    