import re

def prepare_string(line):
    """
    That function takes a line from an input file and prepares it to be
    parsed to the function which creates gene from a string of DNA.
    """
    line = line.upper()
    re.sub('[^ACTG]','', line)
    for char in line.upper().strip():
        if (char != 'A' and char !='C' and char != 'G' and char != 'T'):
            print("At least one of DNA char is wrong")
            return ValueError
    re.sub('[^ACTG]','', line)
    return line
