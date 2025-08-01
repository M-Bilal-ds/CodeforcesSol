for _ in range (int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    count=0
    cx=x.count(1)
    if cx%2==0:
        count+=cx//2
    else:
        count+=(cx//2)+1
    for i in range (n):
        if x[i]>1:
            count+=1
    print(count)
