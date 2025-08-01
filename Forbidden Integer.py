for i in range (int(input())):
    n,k,x=list(map(int,input().split()))
    total=k
    count=0
    store=[]
    if x==k and k!=1:
        k=x-1
        total=x-1
    if k==1 and x==1:
        print('NO')
    elif n==k:
        print('YES')
        print('1')
        print(n)
    elif n>k and x!=1:
        while total<=n:
            total+=k
            count+=1
            store.append(str(k))
        if total==n+k:
            print('YES')
            print(count)
            for i in range (len(store)):
                print(store[i],end=' ')
            print()
        elif total<n+k:
            count+=(n+k)-total
            for i in range ((n+k)-total):
                store.append('1')
            print('YES')
            print(count)
            for i in range (len(store)):
                print(store[i],end=' ')
            print()
    elif n>k and x==1:
        while total<=n:
            total+=k
            count+=1
            store.append(str(k))
        if total==n+k:
            print('YES')
            print(count)
            for i in range (len(store)):
                print(store[i],end=' ')
            print()
        elif total<n+k:
            if ((n+k)-total)%2==0:
                count+=((n+k)-total)//2
                for i in range (((n+k)-total)//2):
                    store.append('2')
                print('YES')
                print(count)
                for i in range (len(store)):
                    print(store[i],end=' ')
                print()
            elif ((n+k)-total)%2==1 and (n+k)-total>2 and x!=3:
                store.append('3')
                count+=((n+k)-total)//2
                for i in range ((((n+k)-total)//2)-1):
                    store.append('2')
                print('YES')
                print(count)
                for i in range (len(store)):
                    print(store[i],end=' ')
                print()
            elif ((n+k)-total)%2==1 and (n+k)-total>2:
                store.append('3')
                count+=((n+k)-total)//2
                for i in range ((((n+k)-total)//2)-1):
                    store.append('2')
                print('YES')
                print(count)
                for i in range (len(store)):
                    print(store[i],end=' ')
                print()
            elif ((n+k)-total)%2==1 and k>2:
                print('YES')
                print(n//2)
                if n%2!=0:
                    print('3',end=' ')
                    for i in range ((n//2)-1):
                        print('2',end=' ')
                    print()
                else:
                    for i in range (n//2):
                        print('2',end=' ')
                    print()
            else:
                print('NO')
