#
# Solution to Project Euler Problem 1
# https://projecteuler.net/problem=1

#
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.                      
# Find the sum of all the multiples of 3 or 5 below 1000. 


def solve():
    """ 
    the answer is 233168
    from https://github.com/luckytoilet/projecteuler-solutions/blob/master/Solutions.md
    >>> solve()
    233168
    """
    
    answer = 0
    for i in range(0,1000):
        if ((i % 3) == 0 ) or ((i % 5) == 0):
            answer = answer + i

    return(answer)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

