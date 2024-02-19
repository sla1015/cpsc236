# -*- coding: utf-8 -*-
"""
tax calculations
"""
TAX_RATE = 0.06

def calcTax(totalCost):
    '''takes argument of totalCost to calculate sales tax and returns tax'''
    tax = totalCost * TAX_RATE
    tax = round(tax, 2)
    return tax

def finalCost(totalCost, totalTax):
    '''sums arguments of totalCost and totalTax to get net total, 
    returns total'''
    total = totalCost + totalTax
    total = round(total, 2)
    return total