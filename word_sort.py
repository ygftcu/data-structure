import sys


def input() :
    return sys.stdin.readline()

n = int(input())
word = []

for i in range(n) :
    word.append(input().strip())

word = list(set(word))
word.sort()
word.sort(key= len)

for i in word:
    print(i)
