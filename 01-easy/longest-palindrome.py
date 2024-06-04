# problem 409

def longestPalindrome(s):

    # adding character frequencies to dictionary
    char_dict = {}
    for a in s:
        if a in char_dict:
            char_dict[a] += 1
        else:
            char_dict[a] = 1

    is_odd = False
    length = 0

    # length of longest palindrome
    for count in char_dict.values():
        # if length is even
        if length % 2 == 0:
            length += count
        else:
            length += count - 1
            is_odd = True

    if is_odd:
        length = length + 1
    
    return length


s1 = "abccccdd"
s2 = "a"
print(longestPalindrome(s1))  # Output: 7
print(longestPalindrome(s2))  # Output: 1
    
