import re 

NUM_OR_DOT_REGEX = re.compile(r'^[\d.]$')

def isNumOrDot(string):
    return bool(NUM_OR_DOT_REGEX.search(string))

def convertToNumber(string):
    number = float(string)
    if number.is_integer():
        number = int(number)
    return number

def isValidNumber(string):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        return
    return valid

def isEmpty(string):
    return len(string) == 0