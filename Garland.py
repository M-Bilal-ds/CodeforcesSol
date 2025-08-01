for _ in range (int(input())):
    x=input()
    if x.count(x[0])==3 or x.count(x[1])==3:
        print('6')
    else:
        print('-1' if len(set(x))==1 else('4' if len(set(x))==4 or len(set(x))==3 or len(set(x))==2 else '4'))
