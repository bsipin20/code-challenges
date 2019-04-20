

def get_product(array):
    """
    >>> get_product([1,2,3,4,5])
    [120, 60, 40, 30, 24]
    """

    new_array = []
    for i in range(0,len(array)-1):
        copy = array
        del copy[i]
        total = 1
        for x in copy:
            total *= x
        new_array.append(total)

    return(new_array)


if __name__ == "__main__":
        import doctest
        doctest.testmod()

