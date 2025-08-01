for _ in range (int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    sum=0
    if len(set(li))==1:
        print('0')
    else:
        for i in range (len(li)//2):
            sum+=max(li)-min(li)
            ind=li.index(max(li))
            li.pop(ind)
            ind=li.index(min(li))
            li.pop(ind)
        print(sum)
            
