x=int(input())
for i in range (x):
    a,b,c=map(int,input().split())
    t_e1=a-1
    if b<c:
        t_e2=(b+(2*(c-b)-1))
    elif b>c:
        t_e2=b-1
    
    if t_e1<t_e2:
        print(1)
    elif t_e1>t_e2:
        print(2)
    elif t_e1==t_e2:
        print(3)
    
