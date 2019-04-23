

def locate_smallest_window(array): # my attempt
    """
    >>> locate_smallest_window([3,7,5,6,9])
    (1, 3)
    >>> locate_smallest_window([3,7,5,6,10,9,15])
    (1, 5)
    """
    left,right = None,None

    first_index = ""
    last_index = ""

    for i in range(0,len(array)-1):

        # finds out if out of order and sets max
        if (array[i] > array[i+1]) & (not first_index):

            first_index = i

        elif (first_index) and (array[i] > array[i+1]):

            last_index = i 

    return((first_index,last_index))

        
            


#        if not (out_ordered_num): 
#            if (array[i+1] < array[i]):
#                first_index = i
#                out_ordered_num = array[i]
#
#        if out_ordered_num:
#            if out_ordered_num < array[i]:
#                print(array[i])
#                print(i)
#                last_index = i 
        
        


    return((first_index,last_index-1))

def window_naive(array): 
    """
    >>> window_naive([3,7,5,6,9])
    (1, 3)
    >>> window_naive([3,7,5,6,10,9,15])
    (1, 5)
    """
 
    left,right = None,None
    s = sorted(array)
    
    for i in range(len(array)):

        # finds out of out of order first time 
        if array[i] != s[i] and left is None:
            left = i

        # sets right time
        elif array[i] != s[i]:
            right = i
    return left,right
    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
