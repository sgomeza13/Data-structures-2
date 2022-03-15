import sys

sys.setrecursionlimit(10**6)


def combinationUtil(arr, n, r, index, data, i, prohibited,isProhibited):
    # Current combination is ready,
    # print it
    if (index == r):
        for x in range(len(prohibited)):
            if (prohibited[x][0] in data and prohibited[x][1] in data):
                isProhibited = True
                break
        if isProhibited == False:    
            for j in range(r): 
                if j+1 < len(data):
                    print( data[j], end = ' ')
                else:
                    print(data[j],end='')
            print()
        return 
     
 
    # When no more elements are
    # there to put in data[]
    if (i >= n):
        return
 
    # current is included, put
    # next at next location

            
        
    data[index] = arr[i]

    combinationUtil(arr, n, r, index + 1,
                    data, i + 1, prohibited,isProhibited)
    
    

    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)

    combinationUtil(arr, n, r, index,
                    data, i + 1, prohibited,isProhibited)



def main():
    topics = []
    no_topic = []
    n = int(input()) 
    w=0
    while w<n:
        tps = input()
        tps = tps.split()
        t = int(tps[0])
        p = int(tps[1])
        s = int(tps[2])
        for i in range(t):  
            topics.append(input().upper())
            topics.sort()
            topics.sort(key=len, reverse=True)
        for j in range(p):
            prohibitedCombination = input().upper()
            no_topic.append(prohibitedCombination.split())
        z = w+1
        print('Set %d:' %z)
        data = [""]*s
        combinationUtil(topics,t,s, 0, data, 0, no_topic,False)
        print()
        topics = []
        no_topic = []
        w = w+1

if __name__ == "__main__":
    main()
