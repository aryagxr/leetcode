# leetcode 75

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''


def isSubsequence(s,t):
    idx = []
    true_count = 0
    if not s:
        return True
    for i in range(len(s)): # ace
        found = False
        for j in range(len(t)):
            if s[i] == t[j]:
                idx.append(j)
                found = True
                break
            if not found:
                return False
    for i in range(len(idx)-1):
        if idx[i] <= idx[i+1]:
            true_count+=1
    if true_count == len(s)-1:
        return True
    return False

        
print(isSubsequence("","ahbgdc"))