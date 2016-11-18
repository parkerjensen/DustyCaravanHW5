#! /usr/bin/env pythons
import sys
from dusty_caravan_task2_hw7 import printBarCode
from urllib.request import urlopen
"""
This script tests the dusty_caravan_task1_hw5.py files method checkDoors
using test input from a csv loaded from the given url.
functions:
    testDoors (loads the url and uses it for the input on running checkDoors)
"""
def testBarCodes():
    """
    Tests the printBarCode function from the dusty_caravan_task2_hw7.py file
    args: NA
    returns: NA
    """
    tests = urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt")
    tests = tests.read().decode()
    tests = tests.splitlines()
    for test in tests:
        print("Entered Zip:",test)
        print(printBarCode(test))    
    
def main():
    """
    Test Function
    """
    testBarCodes()
    return

if __name__=="__main__":
    main()
    exit(0)
