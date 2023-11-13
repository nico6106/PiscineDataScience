def ft_filter(function, values):
    """Function that filters a list. Takes 2 arguments:
   -function: function that will be executed on each value of the list
   -values: all values to be checked"""
    new_values = []
    if function is None:
        return values
    new_values = [val for val in values if function(val)]
    return new_values

    # for val in values:
    #     if function(val):
    #         new_values.append(val)


# def myFunc(x):
#     """function to be applied to the filter"""
#     if x < 18:
#         return False
#     else:
#         return True


# def testing():
#     """testing function to compare filter and ft_filter"""
#     ages = [5, 12, 17, 18, 24, 32]
#     values=ages
#     func=myFunc
#     adults = filter(func, values)
#     adults_bis = ft_filter(func, values)

#     print('filter')
#     for x in adults:
#         print(x)

#     print('My filter')
#     for x in adults_bis:
#         print(x)

# if __name__ == "__main__":
#     testing()
