n = int(input())
for _ in range(n):
     a,b = map(int,input().split())
     x = list(map(int,input().split()))
     print(max(x)-min(x) + min(abs(b-max(x)),abs(b-min(x))))