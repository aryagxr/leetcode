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
        
            
# optimized O[]
            
def two_sum(nums, target):
    my_dict = {}
    length = len(nums)
    for i in range(length):
        my_dict[nums[i]] = i

    



print(two_sum([3,3],6))
