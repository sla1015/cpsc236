# -*- coding: utf-8 -*-
"""
feet/meters conversion functions
"""

def feetToMeters(feet):
    'accepts feet and converts the value to meters'
    meters = feet * 0.3048
    return meters

def metersToFeet(meters):
    'accepts meters and converts the value to feet'
    feet = meters / 0.3048
    return feet
