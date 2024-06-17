# leetcode 75

'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating 
the no-adjacent-flowers rule and false otherwise.
'''

# my first solution :( passed but not optimized at all
def placeFlowers(flowerbed, n):
    three_zeros = True
    count = 0

    for i in range(n): #1,2,3....flowers
        if three_zeros:

            for j in range(len(flowerbed)): #1,0,0,0,1
                print(j)
                # for the first element - prev becomes -1
                prev = j-1
                next = j+1

                # if only one element in the flowerbed
                if len(flowerbed) == 1 and flowerbed[j]==0:
                    flowerbed[j]=1
                    three_zeros = True
                    count += 1

                # check if first two is 0
                if j == 0: #if first element
                    if flowerbed[j] == 0 and flowerbed[next] == 0:
                        flowerbed[j] = 1
                        three_zeros = True
                        count += 1
                
                # check if last two is 0
                if j == len(flowerbed)-1: #if last element
                    if flowerbed[j] == 0 and flowerbed[prev] == 0:
                        flowerbed[j] = 1
                        three_zeros = True
                        count += 1

                # in the middle
                elif flowerbed[j] == 0 and flowerbed[prev] == 0 and flowerbed[next] == 0:
                    flowerbed[j] = 1
                    three_zeros = True
                    count += 1

                else:
                    three_zeros = False
    if count >= n:
        return True
    return False




print(placeFlowers([0,0,1,0,0], 1))

        
