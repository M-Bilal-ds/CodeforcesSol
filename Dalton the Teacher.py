for _ in range (int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    count=0
    for i in range(n):
        if x[i]==i+1:
            count+=1
    print((count+1)//2)
