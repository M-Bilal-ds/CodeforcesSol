for i in range(int(input())):
    n = int(input()) ; s = input()
    res = len(set(s)) ; sum = 0
    for i in range(n,n-res,-1):
        sum += i
    print(sum)
