for _ in range (int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    count=0
    for i in range (n-1):
        if (x[i]%2!=0 and x[i+1]%2!=0) or (x[i]%2!=1 and x[i+1]%2!=1):
            count+=1
    print(count)
