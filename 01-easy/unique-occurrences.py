# leetcode 75

'''
Given an array of integers arr, return true if the number of occurrences 
of each value in the array is unique or false otherwise.
'''

def uniqueOccurrence(arr):
    # dictionary to store num and frequency
    freq_dict = {}
    # check elements and their freq
    for i in arr:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    
    # check if frequencies (values) are unique
    freq_list = []
    for j in freq_dict.values():
        if j in freq_list:
            return False
        else:
            freq_list.append(j)
    return True


print(uniqueOccurrence([1,2,1,1,3]))
        

