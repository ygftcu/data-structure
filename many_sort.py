import sys
from collections import Counter

def input() :
    return sys.stdin.readline()

n, c = list(map(int, input().split()))
num = list(map(int,input().split()))

fre = Counter(num).most_common()

# print(fre)

for i,j in fre:
    for _ in range(j):
        print(i,end=' ')

