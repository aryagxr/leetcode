# using stack

def reverseWords(sentence):
    stack = []
    reversed_str = ""
    for ch in sentence: #last letter added last
        if ch == " ":
            for letter in stack[::-1]:
                reversed_str += letter
                stack.pop(letter)
        stack.append(ch)
    
        # print(stack)
        print(reversed_str)

    

reverseWords("testing words")
