#3 Longest Substring Without Repeating Characters

'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''

def longestSubstring(s):

    start = 0
    max_length = 0
    str_dict = {}
    for i in range(len(s)):
        if s[i] in str_dict and start <= str_dict[s[i]]:
            start = str_dict[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        str_dict[s[i]] = i

    return max_length



    # str_dict = {}
    # print(s[0])
    # substring = ""
    # for i in range(len(s)):
    #     print(s[i])
    #     if s[i] in str_dict:
    #         continue
    #     else:
    #         for j in range(i,len(s)):
    #             if s[j] in substring:
    #                 break
    #             else:
    #                 substring += s[:j+1]
    #                 str_dict[substring] = len(substring)
    #                 print(str_dict)



print(longestSubstring("kwerkerty"))
    

        

    