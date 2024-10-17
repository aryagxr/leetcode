
from collections import defaultdict

def groupAnagrams(strs):

    my_dict = defaultdict(list)
    for s in strs:
        count = [0]*26
        for ch in s: #looping through each alphabet
            # map a to idx 0 and z to 25
            # e-a = 101-97 -> a=0,b=1...e=4..z=25
            count[ord(ch)- ord("a")] += 1 
        my_dict[tuple(count)].append(s)
    return my_dict.values()




print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))