import copy

# Initial solution
# Time = O(n)2
# Space equal O(n)???

#mark own solution written 20.04.2019
def get_product(array):
    """
    >>> get_product([1,2,3,4,5])
    [120, 60, 40, 30, 24]
    """

    new_array = []

    for i in range(0,len(array)):
        new = copy.deepcopy(array)
        del new[i]
        total = 1

        for x in new:
            total *= x


        new_array.append(total)

    return(new_array)


# Time = O(n)
# Space = O(n)

#mark book solution written 20.04.2019

def products(nums):

    """
    What are the core concepts? What other problems might they apply?
    Core concepts: precomputing results from subarrays and then using those to build a solution
 

    >>> get_product([1,2,3,4,5])
    [120, 60, 40, 30, 24]
    """
       

    # Generate prefix products.
    prefix_products = []

    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    
    # Generate suffix products

    suffix_products = []

    for num in reversed(nums):

        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))


    #generate rseult from the product of prefixes and suffixes
    
    results = []
    for i in range(len(nums)):
        if i == 0: # If first element
            results.append(suffix_products[i + 1])
        elif i == len(nums) -1: # If last element
            results.append(prefix_products[i - 1])
        else: # in between elements product before and after
            results.append(
                prefix_products[i-1] * suffix_products[i + 1]
            )

    return(results)
        


if __name__ == "__main__":
        import doctest
        doctest.testmod()

