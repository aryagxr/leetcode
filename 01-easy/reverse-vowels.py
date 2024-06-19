# leetcode 75

'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can
 appear in both lower and upper cases, more than once.
'''


def reverseVowels(s):
    reversed_string = ""
    vowel_list = ['a','e','i','o','u','A','E','I','O','U']
    vowels = []
    for i in s:
        if i in vowel_list:
            vowels.append(i)
            print(vowels)

    for i in s:
        if i in vowel_list:
            reversed_string += vowels.pop() #will pop from end
        else: #if consonent
            reversed_string += i

    return reversed_string



print(reverseVowels("aero"))





#def reverseVower(s):
    # first solution - worked for some test cases
    # vowel_list = ['a','e','i','o','u','A','E','I','O','U']
    # vowel_index = len(s)-1
    # reversed_string = ""
    # for i in s:
    #     if i not in vowel_list: #if i is consonent
    #         reversed_string += i

    #     # for j in range(len(s)-1,0,-1):
    #     for j in range(vowel_index,-1,-1):
    #         vowel_index -= 1
    #         if s[j] in vowel_list:
    #             reversed_string += s[j]
    #         break
    # return reversed_string

    

    







