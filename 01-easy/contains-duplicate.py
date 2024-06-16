def containsDuplicate(nums):

    duplicate = set()
    for num in nums:
        if num in duplicate:
            return True
        duplicate.add(num)
    return False

    # using recursion

    # pop an element
    # for i in range(len(nums)):
    #     num = nums.pop(i)
    #     print(num)
    #     print(nums)
    #     if num in nums:
    #         return True
    #     else:
    #         if len(nums) != 0:
    #             containsDuplicate(nums)
    # return False

print(containsDuplicate([1,2,3,4]))
