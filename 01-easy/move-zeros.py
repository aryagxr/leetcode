# leetcode 75

'''
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

# modify nums in place
def moveZeros(nums):
    zeros = []
    count = 0 # to count how many times we removed
    for i in range(len(nums)):
        i = count
        print(i)
        if nums[i] == 0:
            zeros.append(nums[i])
            nums.remove(nums[i])
            print(nums)
        else:
            count+=1
    nums.extend(zeros)
    return nums
    



# creating a copy of the array
def moveZeros2(nums):
    moved_zeros = []
    zeros = []
    for i in nums:
        if i == 0:
            zeros.append(i)
            # print(zeros)
    for i in nums:
        if i not in zeros:
            moved_zeros.append(i)
            
    moved_zeros.extend(zeros)
    # print(moved_zeros)
    return moved_zeros

print(moveZeros([0,0,1,0,3,12]))