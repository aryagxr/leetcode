def containsDuplicate(nums):

    duplicate = set()
    for num in nums:
        if num in duplicate:
            return True
        duplicate.add(num)
    return False



def containsDuplicates2(nums):
    num_set = set()
    for i in nums:
        if i in num_set:
            return True
        num_set.add(i)
    return False

print(containsDuplicate([1,2,3,4,3]))