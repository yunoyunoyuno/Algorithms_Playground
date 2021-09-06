def matmultiply(A,B):
    p = len(A); r = len(B); q = len(B[0]); C = [[0 for _ in range(q)] for _ in range(p)]
    for i in range(p):
        for j in range(q):
            for k in range(r): C[i][j] += A[i][k] * B[k][j];
    return C;

def matrixMul(A,p):
    K = mcm(p); ans = mmR(A,K,0,len(p)-2);print("If you multiply all these matrices");[print(e) for e in A];print("You will get",ans);

# Bottom Up (Matrix Chain Multiplication)
def mcm(p):
    n = len(p); M = [[0  for i in range(n-1)] for j in range(n-1)];
    K = [[0  for i in range(n-1)] for j in range(n-1)];
    for d in range(1,n-1):
        for i in range(1,n-d):
            j = i + d; M[i-1][j-1] = 1e12;
            for k in range(i,j):
                t = M[i-1][k-1] + M[k][j-1] + p[i-1]*p[j]*p[k];
                if(t < M[i-1][j-1]): K[i-1][j-1] = k; M[i-1][j-1] = t;
    return K
def mmR(A,K,i,j):
    if(i == j): return A[i];
    X = mmR(A,K,i,K[i][j]-1); Y = mmR(A,K,K[i][j],j);
    return matmultiply(X,Y);

M1 = [[3,2],[2,1],[4,3]]; M2 = [[2,3],[1,4]]; M3 = [[1,4],[5,12]];
A = [M1,M2,M3]; p = [3,2,2,2]; M = [ [ 0 for i in range(len(p)-1)] for j in range(len(p)-1)];
m = matrixMul(A,p);

#TopDown + Memoization.
def mB(p,i,j,M):
    if(i >= j) : return 0;
    if(M[i-1][j-1] > 0): return M[i-1][j-1];
    M[i-1][j-1] = 1e10;
    for k in range(i,j):
        M[i-1][j-1] = min(M[i-1][j-1],mB(p,i,k,M) + mB(p,k+1,j,M) + p[i-1]*p[j]*p[k])
    return M[i-1][j-1];
r = mB(p,1,len(p)-1,M);