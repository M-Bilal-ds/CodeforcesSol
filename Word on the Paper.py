for _ in range (int(input())):
    word=[]
    for i in range (8):
        x=input()
        for i in x:
            if i!='.':
                word.append(i)
    for i in word:
        print(i,end='')
    print()
        
