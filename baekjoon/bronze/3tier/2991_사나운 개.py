# https://www.acmicpc.net/problem/2991

A, B, C, D = map(int, input().split())
delivery = list(map(int, input().split()))

for i in delivery:
    dog = 0
    if 0 < i % (A + B) <= A: #사이클 내에서 짖는 시간 내에 오는가
        dog += 1
    if 0 < i % (C + D) <= C:
        dog += 1
        
    print(dog)