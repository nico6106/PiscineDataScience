import sys
from ft_filter import ft_filter


def my_function(str, nb):
    """"Function used to filter my arg"""
    if (len(str) > nb):
        return True
    return False


def check_arg():
    """Check if arguments are corrects. Execute the filter function if yes"""
    args = sys.argv
    if (len(args) != 3):
        raise AssertionError("the arguments are bad")
    if (not args[2].isnumeric()):
        raise AssertionError("the arguments are bad")
    for c in args[1]:
        if not (c.islower() or c.isupper() or c.isdigit() or c == ' '):
            raise AssertionError("the arguments are bad")
    str_split = args[1].split(" ")
    nb = int(args[2])
    new_arg = ft_filter(lambda x: my_function(x, nb), str_split)
    new_list = list(new_arg)
    print(new_list)
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
