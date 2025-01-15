import sys

def input() :
    return sys.stdin.readline()
# memo = []
# def f(n) :
#     global count0
#     global count1
#     if n == 0 :
#         count0 += 1
#         return 0
#
#     elif n == 1 :
#         count1 += 1
#         return 1
#     else:
#         temp = f(n-1) + f(n-2)
#         memo[n] = temp
#         return temp
#
#
# t = int(input())
# for i in range(t) :
#     count0 = 0
#     count1 = 0
#     n = int(input())
#     f(n)
#     print(count0,count1)

t = int(input())

for _ in range(t):
    N = int(input())

    DP = [[]]*41
    DP[0] = [1,0]
    DP[1] = [0,1]
    DP[2] = [1,1]

    for i in range(3, N+1):
        DP[i] = [DP[i-1][0]+DP[i-2][0],DP[i-1][1]+DP[i-2][1]]

    print(DP[N][0], DP[N][1])