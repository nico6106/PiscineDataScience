from typing import Any


def check_tuple(list) -> bool:
    """check if correct input"""
    if list is None:
        return False
    if len(list) == 0:
        return False
    for elem in list:
        if type(elem) is not int:
            return False
    return True


def check_cmd(input) -> bool:
    """check if command is possible"""
    accepted = ['mean', 'median', 'quartile', 'std', 'var']
    if accepted.count(input) == 0:
        return False
    return True


def ft_mean(values):
    """compute mean of values"""
    count = 0
    result = 0
    i = 0
    for elem in values:
        count = count + elem
        i += 1
    if i != 0:
        result = count / i
    print(f"mean : {result}")


def ft_median(values):
    """compute median of values"""
    new_values = list(values)
    new_values.sort()
    len_val = len(new_values)
    
    if len_val % 2 == 0:
        result = new_values[int(len_val / 2)]
    else:
        result = new_values[int(len_val / 2)]
    
    print(f"median : {result}")

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """compute the statistics"""
    if not (check_tuple(args)):
        print('ERROR')
        return
    # exec cmds
    cmds = kwargs.values()
    for cmd in cmds:
        match cmd:
            case 'mean':
                ft_mean(args)
            case 'median':
                ft_median(args)
            case 'quartile':
                ft_mean(args)
            case 'std':
                ft_mean(args)
            case 'var':
                ft_mean(args)
    # print(kwargs, type(kwargs))
    print('ok')
    return
