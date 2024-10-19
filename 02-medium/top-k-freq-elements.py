#347


def topKFrequent(nums, k):
    num_dict = {}
    output=[]
    freq = [[] for i in range(len(nums)+1)]
    
    for n in nums:
        num_dict[n] = 1+num_dict.get(n,0)
        
    for number, count in num_dict.items():
        freq[count].append(number)
        
    for a in range(len(freq)-1, 0,-1):
        #print(a)
        for n in freq[a]:
            output.append(n)
            if len(output) == k:
                return output

    
    
    


print(topKFrequent([1,1,3,3,3,2],2))















# def topKFrequent(nums,k):
#     num_dict = defaultdict(int)
#     max_list = []
#     for i in nums:
#         num_dict[i] += 1
#         print(num_dict)
    
#     for n in range(k): 
#         l = max(num_dict.values())
        
#         print(max_list)
#         # del num_dict[max_list[n]]

#     return max_list


#print(topKFrequent([-1,-1],1))