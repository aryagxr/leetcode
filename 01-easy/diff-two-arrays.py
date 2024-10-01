# 2215

'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
'''

def findDiff(nums1, nums2):
    answer = []
    nums1=set(nums1)
    nums2=set(nums2)
    diff1 = []
    for num in nums1:
        if num not in nums2:
            diff1.append(num)
            # print(diff1)
    diff2 = []
    for num in nums2:
        if num not in nums1:
            diff2.append(num)
    answer.append(diff1)
    answer.append(diff2)
    return answer

print(findDiff([1,2,3,5],[2,3,4]))


