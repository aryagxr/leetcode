# LEETCODE problem 287


def findDuplicate(nums):
    nums2 = []
    for i in range(len(nums)):
        nums2.append(nums[i])
        if i != len(nums)-1 and nums[i+1] in nums2:
            return nums[i+1]




def findDuplicate2(nums):
    nums2=set()
    for i in nums:
        if i in nums2:
            return i
        nums2.add(i)


   





