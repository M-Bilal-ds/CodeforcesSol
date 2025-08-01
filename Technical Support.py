t=int(input())
for i in range (t):
    n=int(input())
    a=input()
    c=0
    for i in range (n):
        if a[i]=='Q':
            c+=1
        if a[i]=='A':
            c-=1
        if c<0:
            c=0
    if c==0:
        print('Yes')
    else:
        print('No')
