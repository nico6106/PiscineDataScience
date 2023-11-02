import sys


def is_number(str) -> bool:
    """check if arg given is a number"""
    i = 0
    if (len(str) == 0):
        return False
    if (str[0] == '-'):
        i += 1
    if (len(str) == i):
        return False
    while (i < len(str)):
        if (not (str[i] >= '0' and str[i] <= '9')):
            return False
        i += 1
    return True


def exec_arg(arg: any):
    """execute the argument that is given"""
    if (not is_number(arg)):
        raise AssertionError("argument is not an integer")
    nb = int(arg)
    if (nb % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return


def handle_arg():
    """check the arguments"""
    args = sys.argv
    if len(args) > 2:
        raise AssertionError("more than one argument is provided")
    if len(args) == 2:
        exec_arg(args[1])
    return


def main():
    """Main function or the program"""
    try:
        handle_arg()
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == '__main__':
    main()
