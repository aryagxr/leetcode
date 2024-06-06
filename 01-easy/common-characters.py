'''
Problem 1002
Given a string array words, return an array of all characters that show up in 
all strings within the words(including duplicates). 
You may return the answer in any order.
'''

def commonChar(words):
    list_of_dicts = []
    for word in words:
        char_dict = {}
        for char in word:
            if char in char_dict: #checks key
                char_dict[char] += 1 #increment the value (freq) by 1
            else:
                char_dict[char] = 1
        list_of_dicts.append(char_dict)
        # print(list_of_dicts)

    # compare dictionaries
    common = []
    first_word = list_of_dicts[0]
    for a in first_word:
        min_count = first_word[a]
        for i in range(1,len(list_of_dicts)):
            if a in list_of_dicts[i]:
                min_count = min(min_count, list_of_dicts[i][a])
            else:
                min_count = 0
                break
        common.extend([a] * min_count)
    return common

        

    
print(commonChar(["bella", "label","roller"]))
