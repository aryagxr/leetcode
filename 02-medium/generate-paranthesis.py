

# if n=3, number of open brackets = 3

def genParenthesis(n):
    stack = []
    output = []

    # recursion function
    def backtrack(open_count,close_count):

        if open_count == close_count == n:
            output.append("".join(stack))
            return #break out of recursion

        
        if open_count < n:
            stack.append("(")
            backtrack(open_count+1, close_count)
            stack.pop()

        if close_count < open_count:
            stack.append(")")
            backtrack(open_count, close_count+1)
            stack.pop()

        
        # initial open and close paranthesis count is 0,0
    backtrack(0, 0)
    return output
        

print(genParenthesis(1))
        




      



