
def twoSumII(numbers, target):
    lp, rp = 0, len(numbers)-1
    while lp<rp:
        c_sum = numbers[lp] + numbers[rp]

        if c_sum > target:
            rp-=1
        elif c_sum < target:
            lp += 1
        else:
            return [lp+1,rp+1]
    return []


print(twoSumII([2,7,11,15],9))