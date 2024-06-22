# leetcode 75

'''
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].
'''

# O(n^2) time complexity
def productArray(nums):
    prod_array = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i!=j:
                prod = prod * nums[j]
        prod_array.append(prod)
    return prod_array


# O(n) time complexity
def productArray2(nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    ans = [1]*len(nums)
    for i in range(1,len(nums)):
        left[i] = left[i-1] * nums[i-1]
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(len(nums)):
        ans[i] = left[i] * right[i]
    return ans


             


print(productArray2([-1,1,0,-3,3]))
        

