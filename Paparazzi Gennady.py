#Python
for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    if n<=2:
        print(1)
    else:
        answere = 1
        a = []
        for i in range(n):
            a.append([i+1,array[i]])
        b = []
        b.append(a[0])
        b.append(a[1])
        l = len(b)
        
        for i in range(2,n):
            while l >=2:
                s1 = (b[l-1][1]-b[l-2][1])/(b[l-1][0]-b[l-2][0])
                s2 = (b[l-1][1]-a[i][1])/(b[l-1][0]-a[i][0])
                if s2>=s1:
                    b.pop()
                    l -= 1
                else:
                    break
            b.append(a[i])
            l += 1
            answere = max(answere,b[l-1][0]-b[l-2][0])
        print(answere)
