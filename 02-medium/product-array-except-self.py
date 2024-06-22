# leetcode 75

'''
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].
'''

def productArray(nums):
    # [1,2,3,4] --> [24,12,8,6]
    # length = len(nums)
    prod = 1
    prod_array = []
    for i in range(len(nums)-1,-1,-1):
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                prod = prod * 1
            prod = prod * nums[j]
        prod_array.append(prod)
        # nums.append(num) 
        print(prod)
    return prod_array[::-1]

        
        
        
        


print(productArray([1,2,3,4]))
        

