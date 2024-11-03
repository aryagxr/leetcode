

def validPalOptimal(s):

    def alnumchar(ch):
        return ord('a')<ord(ch)<ord('z') or ord('A')<ord(ch)<ord('Z') or ord('0')<ord(ch)<ord('9')


    left_pointer = 0
    right_pointer = len(s)-1
    while left_pointer < right_pointer:
        if left_pointer<right_pointer and alnumchar(s[left_pointer]) == True:
            left_pointer+=1
        if right_pointer<left_pointer and alnumchar(s[right_pointer]) == True:
            right_pointer-=1
        if s[left_pointer].lower() != s[right_pointer].lower():
            return False
        return True
        

    



# not optimal
def validPalindrome(s):
    s=s.lower()
    plain_string = ""
    for i in s:
        if i.isalnum():
            plain_string+=i
            print(plain_string)
    
    if plain_string == plain_string[::-1]:
        return True
    return False


print(validPalOptimal("A man, a plan, a canal: Panama"))

