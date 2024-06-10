# 523 Continuous subarray sum

def checkSubarray(nums, k):
    # edge case
    if k == 0:
        return False # no good subarray
    # dictionary for index and rem
    dict = {}
    dict[0] = -1
    pref_sum = 0
    for i in range(len(nums)):
        pref_sum += nums[i] #prefix sum
        rem = pref_sum % k #remainder upto prefix sum


    
    