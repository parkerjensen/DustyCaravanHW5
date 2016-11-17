#! /usr/bin/env pythons
import sys
"""
This script contains methods to check whether doors will open in a minivan based on multiple inputs
functions:
    checkDoors (checks if the doors will open based on the input)
"""
def checkDoors(ld, rd, cl, ml, li, lo, ri, ro, gs):
    """
    This checks all the switches and handles to see whether the door of the van will open
    Args:
        ld: left dashboard switch (1 or 0)
        rd: left dashboard switch (1 or 0)
        cl: child lock switch (1 or 0)
        ml: master lock switch (1 or 0)
        li: left inside handle (1 or 0)
        lo: left outside handle (1 or 0)
        ri: right inside handle (1 or 0)
        ro: right outside handle (1 or 0)
        gs: gear shift position (P, N, D, 1, 2, 3, or R)
    Returns:
        result: string of doors that open
    """
    returnString = ""
    rightOpen = False
    leftOpen = False
    validGears = ['P', 'N', 'D', '1', '2', '3', 'R']
    
    if gs in validGears:
        if gs != 'P':
            return "Both doors stay closed."
    else:
        return "Invalid gear shift position!"

    if int(ml) == 0:
        return "Both doors stay closed."

    if int(lo) == 1 or int(ld) == 1:
        returnString += "Left door opens. "
        leftOpen = True
    elif int(li) == 1 and int(cl) == 0:
        returnString += "Left door opens. "
        leftOpen = True
    
    if int(ro) == 1 or int(rd) == 1:
        returnString += "Right door opens."
        rightOpen = True
    elif int(ri) == 1 and int(cl) == 0:
        returnString += "Right door opens."
        rightOpen = True

    if not rightOpen and not leftOpen:
        return "Both doors stay closed."
    else:
        return returnString
        


def main():
    """
    Test Function
    """
    print(checkDoors(0, 0, 0, 1, 0, 1, 0, 0, 'P'))
    return

if __name__=="__main__":
    main()
    exit(0)
