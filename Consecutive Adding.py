def c(M,C,R,X):
    for i in range(R-X+1,R):
        for j in range(C-X+1,C):
            if X==2:
                if sum([sum([M[p][q](-1)*(R+C-p-q) for q in range(C)]) for p in range(R)])!=0:
                    print('No')
                    break
            elif sum([sum([M[p][q]-M[p][q+j-C+X]-M[p+i-R+X][q]+M[p+i-R+X][q+j-C+X] for q in range(C%X,j,X)]) for p in range(R%X,i,X)])!=0:
                print('No')
                break
        else:                                                
            continue
        break
    else:
        print('Yes')
T=int(input())
for n in range(T):
    R,C,X=[int(j) for j in input().split(' ')]
    A=[]
    B=list(A)
    for i in range(R):
        A.append([int(j) for j in input().split(' ')])
    for i in range(R):
        B.append([int(j) for j in input().split(' ')])
    M=[[A[i][j]-B[i][j] for j in range(C)]for i in range(R)]
    c(M,C,R,X)
