for i in range (int(input())):
    a,n=map(int,input().split())
    b=input()
    c=0
    for i in range (len(b)):
        if b[i]>=str(n):
            c+=1
        else:
            break
    print(b[:c]+str(n)+b[c:])
