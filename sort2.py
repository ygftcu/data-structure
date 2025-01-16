import sys

def input() :
    return sys.stdin.readline()

# n = int(input())
# sort = []
#
# for _ in range(n) :
#     sort.append(int(input()))
#
#
# sort = list(set(sort))
#
# def merge(arr) :
#     if len(arr) < 2 :
#         return arr
#
#     pivot = len(arr) //2
#     start = merge(arr[:pivot])
#     end = merge((arr[pivot:]))
#
#     s = 0
#     e = 0
#     mer = []
#
#     while s < len(start) and e < len(end) :
#         if start[s] < end[e] :
#             mer.append(start[s])
#             s += 1
#
#         else:
#             mer.append(end[e])
#             e += 1
#
#
#     mer += start[s:]
#     mer += end[e:]
#     return mer
#
# merge(sort)
#
# for i in sort:
#     print(i)

N = int(input())
numbers = [int(input()) for _ in range(N)]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    # 비교해서 합치는 과정
    l, h = 0, 0
    merge = []
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merge.append(low[l])
            l += 1
        else:
            merge.append(high[h])
            h += 1

    # 남은 부분은 이미 정렬 되어 있으므로 단순하게 뒤에 붙여준다.
    merge += low[l:]
    merge += high[h:]
    return merge


result = merge_sort(numbers)
print(*result, sep="\n")