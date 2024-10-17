# bruteforce O[n^2]
def twoSum(nums, target):
    output = []
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1,n):
            if nums[j] + nums[i] == target:
                output.append(i)
                output.append(j)
                return output
    return None
        
            
# optimized O[n]
            
def two_sum(nums, target):
    prev_dict = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in prev_dict:
            return [prev_dict[diff], idx]
        prev_dict[num] = idx
    return


print(two_sum([3,3],6))
