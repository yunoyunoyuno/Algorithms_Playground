# Normal C(n,k);
def C1(n,k):
    if(n < k or k < 0): return 0;
    if(n == k or k == 0): return 1;
    return C1(n-1,k) + C1(n-1,k-1);

# Top Down + Mem;
def C2R(n,k,C):
    if(n < k or k < 0): return 0;
    if(n == k or k == 0): return 1;
    if(C[n-1][k-1] > 0): return C[n-1][k-1];
    C[n-1][k-1] = C2R(n-1,k-1,C) + C2R(n-1,k,C);
    return C[n-1][k-1];
def C2(n,k):
    C = [[0 for i in range(n)] for j in range(n)]; return C2R(n,k,C);
    
#Bottom Up
def C3(n,k):
    n += 1; k += 1;
    C = [[0 for i in range(k)] for j in range(n)];
    for i in range(n): C[i][0] = 1;
    for j in range(k): C[j][j] = 1;
    for r in range(2,n):
        for c in range(1,k):
            if(c < r): C[r][c] = C[r-1][c-1] + C[r-1][c];
    return C[n-1][k-1];

n = 6; k = 2;
a = C1(n,k);print(a);
b = C2(n,k); print(b);
c = C3(n,k); print(c);

