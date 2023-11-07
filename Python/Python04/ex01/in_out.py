def square(x: int | float) -> int | float:
    """compute square of x"""
    return x * x


def pow(x: int | float) -> int | float:
    """compute power of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer function"""
    def inner() -> float:
        """inner function"""
        nonlocal x
        count = function(x)
        x = count
        return count
    return inner
