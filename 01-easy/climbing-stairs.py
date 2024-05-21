'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
'''

# using recursion
def fibonacci(n):
    if n <= 1:
        return n
    # else return the sum of previous two numbers
    return fibonacci(n-1) + fibonacci(n-2)


# calls fibonacci function
def climbingStairs(s):
    return fibonacci(s+1)


print(climbingStairs(4))



    

