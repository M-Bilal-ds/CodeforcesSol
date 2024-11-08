for _ in range (int(input())):
    n,k=map(int,input().split())
    print('YES' if n%k==0 else('YES'if n%2==0 or (n-k)%2==0 else 'NO') )
