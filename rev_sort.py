import sys

def input() :
    return sys.stdin.read()

#read로 하는 이유 텍스트를 하나의 문자열로 반환

n, *s = input().split()

for i in range(int(n)) :
    s[i] = s[i][::-1]

s = list(map(int, s))

print(*sorted(s), sep="\n")