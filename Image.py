x=int(input())
for i in range (x):
    x=input()
    y=input()
    q=list(x)
    r=list(y)
    a=q[0]
    b=q[1]
    c=r[0]
    d=r[1]
    if a==b and a==c and a==d:
        print('0')
    elif a!=b and a!=c and a!=d and b!=c and c!=d and b!=d:
        print('3')
    elif (a==b and a!=c and a!=d and c!=d) or (a==c and a!=d and a!=b and b!=d) or (c==d and c!=b and c!=a and a!=b) or (b==d and b!=a and b!=c and a!=c) or (a==d and a!=b and a!=c and b!=c) or (b==c and b!=a and b!=d and a!=d):
        print('2')
    else:
        print('1')
        
