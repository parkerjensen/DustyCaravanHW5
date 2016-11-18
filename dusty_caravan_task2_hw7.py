#! /usr/bin/env pythons
import sys
"""
A file to take zip codes (and digits) and turn them into barcodes.
"""

def printDigit(d):
    """
    Turn a digit into a barcode pattern
    Args:
        d is a digit
    Returns:
        string of the barcode pattern
    """
    try:
        i = int(d)
    except:
        print("This digit is not an integer")
        return ""
    if(i == 1):
        return(":::||")
    if(i == 2):
        return("::|:|")
    if(i == 3):
        return("::||:")
    if(i == 4):
        return(":|::|")
    if(i == 5):
        return(":|:|:")
    if(i == 6):
        return(":||::")
    if(i == 7):
        return("|:::|")
    if(i == 8):
        return("|::|:")
    if(i == 9):
        return("|:|::")
    if(i == 0):
        return("||:::")
    print("This is not a single digit integer!")
    return ""

def printBarCode(zipCode):
    """
    Take a zip code and turns into a bar code
    Args:
        zipCode: a zipcode made of 5 digits
    returns:
        a string of the barcode
    """
    try:
        zip = int(zipCode)
        zip = str(zipCode)
    except:
        print("The zipcode is incorrectly formatted")
        return ""
    if len(zip) != 5:
        print("The zipcode provided is not the proper length (5 digits)")
        return ""
    checktotal = int(zip[0]) + int(zip[1]) + int(zip[2]) + int(zip[3]) + int(zip[4])
    check = checktotal % 10

    barcode = "|"
    barcode += printDigit(zip[0])
    barcode += printDigit(zip[1])
    barcode += printDigit(zip[2])
    barcode += printDigit(zip[3])
    barcode += printDigit(zip[4])
    barcode += printDigit(check)
    barcode += "|"
    return barcode


def main():
    """
    Test Function
    """
    print(printDigit(3))
    print(printDigit("8"))
    print(printDigit("No"))
    print(printDigit("12"))
    print(printBarCode(12345))
    print(printBarCode("123b4"))
    print(printBarCode("123456"))
    return

if __name__=="__main__":
    main()
    exit(0)
