x=int(input())
for i in range (x):
    y=int(input())
    a=list(map(int,input().split()))
    max=0
    sum=0
    for i in range (len(a)):
        if a[i]==0:
            sum+=1
        if sum>max:
            max=sum
        if a[i]==1:
            sum=0
    print(max)
