
def dailyTemp(temperatures):
    output = [0]*len(temperatures) #same length as temperature array
    stack = [] #add temp and index of that temp
    for i,temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackT, stackIdx = stack.pop()
            output[stackIdx] = i-stackIdx
        stack.append([temp,i])
    return output


print(dailyTemp([73,74,75,71,69,72,76,73]))