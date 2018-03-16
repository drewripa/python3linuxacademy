from os import getenv
from math import pi

def _printpi(digits):
    print(str(pi)[:digits+1])

digits = getenv('DIGITS', 10)
_printpi(int(digits))

