# https://www.acmicpc.net/problem/10768

a = int(input())
b = int(input())
if a > 2 :
    print("After")
elif a == 2 and b > 18 :
    print("After")
elif a == 2 and b == 18 :
    print("Special")
else :
    print("Before")