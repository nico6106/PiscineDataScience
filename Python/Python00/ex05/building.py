import sys


def handle_arg(arg):
    """function that count and display data about the text"""
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digits = 0
    for c in arg:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        elif c.isnumeric():
            digits += 1
        else:
            punctuation += 1
    print(f"The text contains {len(arg)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")
    return


def handle_prompt():
    """function that handle the prompt"""
    str = ''
    try:
        str = input('What is the text to count?\n')
        str += '\n'
    except EOFError:
        pass
    return str


def check_arg():
    """function that check if number of arguments is correct
    throw an exception if > 2
    ask for prompt if no arg provided"""
    args = sys.argv
    if (len(args) == 2):
        handle_arg(args[1])
    elif (len(args) > 2):
        raise AssertionError("more than one argument is provided")
    else:
        msg_prompt = handle_prompt()
        handle_arg(msg_prompt)


def main():
    """Main function or the program"""
    try:
        check_arg()
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()
