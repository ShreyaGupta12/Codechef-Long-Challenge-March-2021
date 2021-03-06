#Python
from collections import deque
p = 10 ** 9 + 7
facts = [1] * (5 * (10 ** 5) + 10)
invfacts = [1] * (5 * (10 ** 5) + 10)
for i in range(1, len(facts)):
    facts[i] = (facts[i - 1] * i) % p
    invfacts[i] = pow(facts[i], p - 2, p)
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    graph=[[] for i in range(n)]
    edges=[0 for i in range(n)]
    for i in range(n-1):
        u,v=map(int,input().split())
        u,v=u-1,v-1
        graph[u].append(v)
        graph[v].append(u)
        edges[u]+=1
        edges[v]+=1
    edges[0]+=2
    par=[-1 for i in range(n)]
    que=deque([0])
    while(que):
        i=que.popleft()
        for j in graph[i]:
            if j!=par[i]:
                par[j]=i
                que.append(j)
    count=[1 for i in range(n)]
    d=[1 for i in range(n)]
    que=deque([])
    for i in range(n):
        if edges[i]==1:
            que.append(i)
    while(que):
        i=que.popleft()
        d[i]=(d[i]*facts[count[i]-1])%p
        edges[par[i]]-=1
        count[par[i]]+=count[i]
        d[par[i]]=(((d[par[i]]*invfacts[count[i]])%p)*d[i])%p
        if edges[par[i]]==1:
            que.append(par[i])
    d[0]=(d[0]*facts[count[0]-1])%p
    res=[]
    anst=[0 for i in range(n)]
    anst[0]=d[0]
    res.append([1,0])
    ans=[0 for i in range(n)]
    ans[0]=1
    que=deque([(0,-1)])
    while(que):
        i,parent=que.popleft()
        for j in graph[i]:
            if j!=parent:
                c=count[j]
                ans[j]=ans[i]*c/(n-c)
                anst[j]=int(anst[i]*c*pow(n-c,p-2,p))%p
                res.append([ans[j],j])
                que.append((j,i))
    res.sort(key=lambda x:(x[0],x[1]),reverse=True)
    print(res[k-1][1]+1,anst[res[k-1][1]])
