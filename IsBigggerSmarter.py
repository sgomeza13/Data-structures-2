from sys import stdin
elephants = []
cont = 1

for line in stdin:
    elephant = [int(x) for x in line.split()]
    elephant.append(cont)
    elephants.append(elephant)
    cont += 1 

elephants.sort(key=lambda elephants:elephants[1], reverse=True)

def findLIS(arr):
 
    # base case
    if not arr:
        return []
      
    if len(elephants) == 1:
        print(1)
        print(1)
        return []
    
  
    # LIS[i] stores the longest increasing subsequence of sublist
    # `arr[0…i]` that ends with `arr[i]`
    LIS = [[] for _ in range(len(arr))]
 
    # LIS[0] denotes the longest increasing subsequence ending at `arr[0]`
    LIS[0].append(arr[0])
 
    # start from the second element in the list
    for i in range(1, len(arr)):
 
        # do for each element in sublist `arr[0…i-1]`
        for j in range(i):
 
            # find the longest increasing subsequence that ends with `arr[j]`
            # where `arr[j]` is less than the current element `arr[i]`
 
            if arr[j][0] < arr[i][0] and arr[j][1] > arr[i][1] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()
 
        # include `arr[i]` in `LIS[i]`
        LIS[i].append(arr[i])
 
    # `j` will store the index of LIS
    j = 0
    for i in range(len(arr)):
        if len(LIS[j]) < len(LIS[i]):
            j = i
 
    # print LIS
    resp = LIS[j]
    print(len(resp))
    for i in range(len(resp)):
        print(resp[i][2])
 
 
findLIS(elephants)