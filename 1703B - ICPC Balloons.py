t = int(input())
for _ in range (t):
    n = int(input())
    s = input()
    dict = {} 
    count = 0
    for i in s:
        if i not in dict:
            dict[i] = True
            count += 2
        else:
            count += 1
    print(count)
            
        