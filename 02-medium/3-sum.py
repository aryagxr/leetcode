
def threeSum(numbers):
    output = []
    numbers.sort()
    # print(numbers)

    for i, a in enumerate(numbers):
        if a > 0:
            break
        if i > 0 and a == numbers[i-1]:
            continue

        lp, rp = i+1, len(numbers)-1
        while lp < rp:
            three_sum = a + numbers[lp] + numbers[rp]
            if three_sum > 0:
                rp -= 1
            elif three_sum < 0:
                lp += 1
            else:
                output.append([a,numbers[lp],numbers[rp]]) 
                lp += 1
                rp -= 1
                while numbers[lp] == numbers[lp-1] and lp < rp:
                    lp += 1

    return output
    





print(threeSum([-1,0,1,2,-1,-4]))