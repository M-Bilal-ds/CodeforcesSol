for i in range(int(input())):
    m,n,rb,cb,rd,cd=map(int,input().split())
    a=[]
    if rd>=rb:
        a.append(rd-rb)
    else:
        a.append(2*(m-rb)+rb-rd)
    if cd>=cb:
        a.append(cd-cb)
    else:
        a.append(2*(n-cb)+cb-cd)
    print(min(a))
        
