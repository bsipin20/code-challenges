



def locate_smallest_win(array):
    """
    >>> locate_smallest_win([3,7,5,6,9])
    (1, 3)
    """
    
    left,right= None,None
    n = len(array)
    max_seen ,min_seen = -float('inf'),float('inf')

    for i in range(n):
        max_seen = max(max_seen,array[i])
        if array[i] < max_seen:
            right = i

    for i in range(n-1,-1,-1):
        min_seen = min(min_seen,array[i])
        if array[i] > min_seen:
            left = i
    return left,right
    
 

if __name__ == "__main__":
    import doctest
    locate_smallest_win([3,7,5,6,9])
    doctest.testmod()


