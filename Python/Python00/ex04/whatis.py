import sys


def print_error(error):
    print(f"AssertionError: {error}")


def is_number(str) -> bool:
    i = 0
    if (len(str) == 0):
        return False
    if (str[0] == '-'):
        i += 1
    while (i < len(str)):
        if (not (str[i] >= '0' and str[i] <= '9')):
            return False
        i += 1
    return True


def handle_arg(arg: any):
    if (not is_number(arg)):
        print_error('argument is not an integer')
        return
    nb = int(arg)
    if (nb % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return


if __name__ == '__main__':
    args = sys.argv
    assert len(args) > 2, "more than one argument is provided"
    if len(args) == 2:
        handle_arg(args[1])
