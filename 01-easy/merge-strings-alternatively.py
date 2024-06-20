# leetcode 75

'''
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the 
end of the merged string. Return the merged string.
'''

def mergeStrings(word1, word2):
    merged_string = []
    list1 = list(word1)
    list2 = list(word2)
    while list1:
        merged_string += list1.pop(0)
        if list2:
            merged_string += list2.pop(0)
    merged_string.extend(list2)
    merged_string = ''.join(map(str, merged_string))
    return merged_string
        
        

        
print(mergeStrings("abcd","pq"))

    