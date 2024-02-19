# -*- coding: utf-8 -*-
"""
tax input and output
"""

def taxTitle():
    """prints title"""
    print("Sales Tax Calculator")

def getTotal():
    '''gets input of cost of items and adds them together'''
    print("\nENTER ITEMS (ENTER 0 TO END)")
    cost = 1
    total = 0
    while cost != 0:
        cost = float(input("Cost of item: "))
        total += cost
        
    return total

def display(subtotal, tax, net):
    """displays net and subtotals, along with total sales tax"""
    print("Subtotal:", subtotal, "\nSales Tax:", tax, 
          "\nTotal after tax:", net)



def main():
   total = getTotal()
   print(total)


   
if __name__ == "__main__":
    main()