# problem 169

def majorityElement(nums):
    major = None
    count = 0
    for num in nums:
        if count == 0:
            major = num
            count = 1
        elif num == major:
            count = count + 1
        else:
            count = count - 1
    return major


print(majorityElement([5,6,5,6,5]))
        