import sys

def input() :
    return sys.stdin.readline()

n = int(input())
sort = []
for i in range(n) :
    sort.append(int(input()))

sort = list(set(sort))

def quick(sort, start, end) :
    if start >= end :
        return

    pivot = start
    left = start +1
    right = end

    while left <= right :

        while left <= end and sort[left] <= sort[pivot] :
            left += 1

        while right > start and sort[right] >= sort[pivot] :
            right -= 1

        if left > right :
            sort[right], sort[pivot] = sort[pivot], sort[right]

        else:
            sort[left], sort[right] = sort[right], sort[left]


    quick(sort,start,right-1)
    quick(sort,right+1,end)

quick(sort,0,len(sort)-1)

for i in sort :
    print(i)