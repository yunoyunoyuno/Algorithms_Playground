def mat2dimMultp(M1,M2):
    R = [[None,None],[None,None]]
    for i in range(2):
        for j in range(2):
            R[i][j] = M1[i][0]*M2[j][0]+ M1[i][1]*M2[j][1]
    return R;

F = [[0,1],[1,1]];

def FR(n):
    if(n==1): return F;
    m = FR(n//2);
    if(n % 2 == 0): return mat2dimMultp(m,m)
    t=  mat2dimMultp(m,m)
    return mat2dimMultp(F,t)
    
def fib(n):
    A = FR(n);
    return A[0][1]
    
ans = fib(5);
