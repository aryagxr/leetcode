# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

def isValid(s):

    stack = []
    dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in s:
        if char in dict: # checks existence of char in dict keys
            # it is an closing bracket
            top_element = stack.pop() if stack else '#' #remove top most stack element
            if dict[char] != top_element: #if char corresponding open bracket same as top element open bracket
                return False
            
        else: # if closing bracket, check if corresponding opening bracket is in stack
            stack.append(char) # add the opening bracket to stack
            
        # if nothing is in stack, stack = false, empty, all brackets are matched
    return not stack #true



print(isValid('()'))

        
            



