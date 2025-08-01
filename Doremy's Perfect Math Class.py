from math import gcd
for _ in range (int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    check=0
    for i in range (n):
        check=gcd(check,s[i])
    print(max(s)//check)    
