# Given a non-negative integer c, 
# decide whether there're two integers a and b such that a2 + b2 = c.

from cmath import sqrt


def sumSquare(c):
    upper_bound = int(sqrt(c))
    lower = 0
    while lower <= upper_bound:
        sum_of_sq = (lower*lower) + (upper_bound*upper_bound)
        if sum_of_sq == c:
            return True
        elif sum_of_sq < c:
            lower += 1
        else:
            upper_bound -= 1
        
    return False
        

print(sumSquare(7))
    