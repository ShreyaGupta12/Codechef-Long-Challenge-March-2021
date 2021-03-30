for _ in range(int(input())):
    c=0
    s=input()
    if s[0]=='1':
        c+=1
    for i in range(1,len(s)):
        if s[i]=='1'and s[i]!=s[i-1]: c+=1
    print (c)
