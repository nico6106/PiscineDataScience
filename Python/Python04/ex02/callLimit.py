def callLimit(limit: int):
    count = 0
    print(f"count={count} limit={limit}")
    def callLimiter(function):
        nonlocal count
        count = count + 1
        if (count > limit):
            print(f"Error: {function.__str__} call too many times")
            return
        else:
            function()
            print('executed')
            return
        # def limit_function(*args: Any, **kwds: Any):
    return callLimiter()
