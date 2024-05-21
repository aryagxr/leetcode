'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
'''

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if target > nums[i] and target < nums[len(nums)-1]:
                i=i+1
            elif target > nums[len(nums)-1]: # if target is greater than last number in list
                return len(nums)
            else:
                return i



print(searchInsert([1,3,4,5],6))

