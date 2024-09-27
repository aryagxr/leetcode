# 724 


def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i
        left_sum += nums[i]

    return -1




print(pivotIndex([1,2,3]))
