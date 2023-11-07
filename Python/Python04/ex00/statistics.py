from typing import Any


def check_tuple(list) -> bool:
    """check if correct input"""
    if list is None:
        return False
    if len(list) == 0:
        return False
    for elem in list:
        if not(type(elem) is int or type(elem) is float):
            return False
    return True


def check_cmd(input) -> bool:
    """check if command is possible"""
    accepted = ['mean', 'median', 'quartile', 'std', 'var']
    if accepted.count(input) == 0:
        return False
    return True


def ft_mean(values, show: bool = False):
    """compute mean of values"""
    if not (check_tuple(values)):
        print('ERROR')
        return
    count = 0
    result = 0
    i = 0
    for elem in values:
        count = count + elem
        i += 1
    if i != 0:
        result = count / i
    if show:
        print(f"mean : {result}")
    return result


def ft_median(values) -> float:
    """compute median of values"""
    if not (check_tuple(values)):
        print('ERROR')
        return
    new_values = list(values)
    new_values.sort()
    len_val = len(new_values)
    index = int(len_val / 2)
    if len(new_values) % 2 == 0:
        result = (new_values[index - 1] + new_values[index]) /2
    else:
        result = new_values[int(len_val / 2)]
    
    print(f"median : {result}")
    return result


def ft_std(values):
    """compute standard deviation"""
    if not (check_tuple(values)):
        print('ERROR')
        return
    var = ft_var(values)
    result = var ** 0.5
    print(f"std : {result}")


def ft_var(values, show: bool = False):
    """compute variance"""
    if not (check_tuple(values)):
        print('ERROR')
        return
    mean = float(ft_mean(values))
    sum = 0.0
    for x in values:
        sum = sum + (float(x) - mean) * (float(x) - mean)
    result = ((1 / len(values)) * sum)
    if show:
        print(f"var : {result}")
    return result


def ft_quartile(values):
    if not (check_tuple(values)):
        print('ERROR')
        return
    new_values = list(values)
    new_values.sort()
    len_val = len(new_values)
    
    index = int(len_val / 2)
    if index % 2 == 0:
        result = (new_values[index - 1] + new_values[index]) /2
    else:
        result = new_values[index]
    
    result = 0
    print(f"quartile : {result}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """compute the statistics"""
    # exec cmds
    cmds = kwargs.values()
    for cmd in cmds:
        match cmd:
            case 'mean':
                ft_mean(args, True)
            case 'median':
                ft_median(args)
            case 'quartile':
                ft_quartile(args)
            case 'std':
                ft_std(args)
            case 'var':
                ft_var(args, True)
    # print(kwargs, type(kwargs))
    return
