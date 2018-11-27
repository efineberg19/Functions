#!/ysr/bin/python
#utility.py

'''(docstring comment describing this file)'''

__author__ = "Beth Fineberg"
__version__ = "1.0"

def yes_answer(answer):
    '''returns True if yes, False otherwise'''
    if answer.upper() == "Y" or answer.upper() == "YES":
        return True
    else:
        return False

def get_valid_number(low, high):
    pick = high + 1
    
    while pick < low or pick > high:
        pick = int(input("Please give me a number between", str(low), "and",
                     str(high)))

    return pick
