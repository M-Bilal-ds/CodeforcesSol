from math import gcd
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    mx=(x[0]-1)
    for i in range(1,n):
        mx=gcd(mx,(x[i]-i-1))
    print(mx)



