from itertools import cycle

def infinite(lst, tries):
    result = ''
    tries_lst = cycle(lst)

    if lst:
        for symbol in range(tries):
            result += str(next(tries_lst))
    return result