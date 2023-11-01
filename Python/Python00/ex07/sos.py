import sys


def dictionnary():
    """return MORSE dictionnary"""
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    }
    return NESTED_MORSE


def check_str(str):
    """Check if str is al alphanumeric string"""
    specials = '/*-+.!@#$%^&*()_-+=[];:\'"<,.>?/`~'
    for c in str:
        if not (c.isupper() or c.islower() or c.isdigit() or c == ' '):
            return False
        if specials.find(c.upper()) != -1:
            return False
    return True


def check_arg():
    """Check arg and convert to morse"""
    dic = dictionnary()
    args = sys.argv
    result = ''
    if (len(args) != 2):
        raise AssertionError("only one parameter is expected")
    if not check_str(args[1]):
        raise AssertionError("the arguments are bad")
    str = args[1].upper()
    for c in str:
        result = result + dic.get(c)
    if (len(result) > 0):
        result = result[:-1]
    print(result)
    return


def main():
    """Main function or the program"""
    try:
        check_arg()
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()
