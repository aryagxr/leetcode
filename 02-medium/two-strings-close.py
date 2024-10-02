#1657

def ifStringsAreClose(word1, word2):
    if len(word1) != len(word2):
        return False
    freq1 = {}
    freq2 = {}
    for char in word1:
        freq1[char] = freq1.get(char,0)+1
        # print(freq1)
    for char in word2:
        freq2[char] = freq2.get(char, 0)+1
        # print(freq2)
    set1 = set(freq1.keys())
    set2 = set(freq2.keys())
    if set1 != set2:
        return False
    check_freq1 = sorted(freq1.values())
    check_freq2 = sorted(freq2.values())
    if check_freq1 != check_freq2:
        return False
    # print(check_freq1,check_freq2)
    return True
    
    


print(ifStringsAreClose("abbzzca","babzzcz"))

