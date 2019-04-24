import copy

# Initial solution
# Time = O(n)2
# Space equal O(n)???

#mark own solution written 20.04.2019
def product(array):
    """
    >>> product([1,2,3,4,5])
    [120, 60, 40, 30, 24]
    """
    prefix_products = []
    for num in array:
        if prefix_products:
            prefix_products.append(num * prefix_products[-1])
        else:
            prefix_products.append(num)
    
    suffix_products =[]
    for num in reversed(array):
        if suffix_products:
            suffix_products.append(num*suffix_products[-1])
        else:
            suffix_products.append(num)

    print(suffix_products)
    suffix_products = list(reversed(suffix_products))
    print(suffix_products)

    products_ = []

    for num in range(0,len(array)):

        if num == 0:
            products_.append(suffix_products[num+1])
        elif num == len(array)-1:
            products_.append(prefix_products[num-1])
        else:
            products_.append(
                prefix_products[num-1] * suffix_products[num+1]
                )
    return(products_)



if __name__ == "__main__":
    import doctest
    doctest.testmod()







