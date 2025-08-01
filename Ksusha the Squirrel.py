n,j=map(int,input().split())
r=input()
l=list(r)
count=0
max=0
for i in range (n):
    if l[i]=="#":
        count+=1
        if max<count:
           max=count 
    if l[i]!='#':
        count=0
if max<j:
    print('YES')        
else:
    print('NO')
