from typing import Any


def callLimit(limit: int):
    """decorator that limits a call of a function"""
    count = 0

    def callLimiter(function):
        """limiter that return the limit_function"""

        def limit_function(*args: Any, **kwds: Any):
            """limit function that executes or not the function"""
            nonlocal count
            if count < limit:
                function()
            else:
                print(f"Error: {function} call too many times")
            count = count + 1
            return
        return limit_function
    return callLimiter
