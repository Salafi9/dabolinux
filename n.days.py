#! /usr/bin/env python3
__author__ = 'Ahmad Abdulnasir <dabolinux@gmail.com> www.dabolinux.com'
__copyright__ = 'Copyright (c) 2016, salafi'
__version__ = "0.1t"

from datetime import datetime, timedelta

def nDays(n):

    d = datetime.today() -timedelta(days=n)
    print("The day time stamp is: ", d)
    d_name = d.strftime("%A")
    print("The day name is: ", d_name)

if __name__ == "__main__":
    n  = input("Enter days to travel back to: ")
    nDays( int(n) )
