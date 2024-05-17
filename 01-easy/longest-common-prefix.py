def LongestCommonPrefix(strs):
    common_prefix = ""
    strs = sorted(strs)
    # print(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            common_prefix += first[i]
        else:
            return common_prefix
    return common_prefix


#test case
print(LongestCommonPrefix(["flower","flow","flight"]))
print(LongestCommonPrefix(["dog","racecar","car"]))




