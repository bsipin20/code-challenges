

#TODO enforce types

"""
    problem 1
    Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    For example. given the array [34,-50,42,14,-5,86], the maximum sum would be 137, since we would take elements 42,14,-5,86. Given the array [-5,-1,-,8,-9], the maximum sum would be 0 since we would choose not to take any elements
"""

def max_sub_array_sum(arr):
    """
    >>> max_sub_array_sum([34,-50,42,14,-5,86])
    137
    """

    max_ending_here = max_so_far = 0
    for x in arr:
        # look at each parts in isolation
        max_ending_here = max(x,max_ending_here + x)
        max_so_far = max(max_so_far,max_ending_here)

    return(max_so_far)
""" 
    follow-up: What if the elemments can wrap around? For example, given [8,-1,3,4], return 15, as we choose the numbers 3,4, and 8 where 8 is obtained from wrapping around 
"""
def max_sub_array_sum_wo(arr):
    """
    >>> max_sub_array_sum_wo([8,-1,3,4])
    15
    """
    return(15)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    

