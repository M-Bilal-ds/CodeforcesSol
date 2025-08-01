x=int(input())
a=list(map(int, input().split()))
count=1
a.sort()
for i in range (x-1):
    if a[i+1]-a[i]==1:
        count+=1
        if count==3:
            print('YES')
            exit()
    elif a[i+1]-a[i]>1:
        count=1
else:
    print('NO')
