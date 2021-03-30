#Python
n,h,x=map(int,input().split())
l=list(map(int,input().split()))
if (max(l)+x)>=h : print("YES")
else: print("NO")
