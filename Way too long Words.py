n=int(input())
for i in range (n):
    w=input()
    l=len(w)
    if l>10:
        a=w[0]
        b=w[-1]
        print(f'{a}{l-2}{b}')
    else:
        print(f'{w}')
