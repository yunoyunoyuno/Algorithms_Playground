#N-Queen;
def findQ(n): nQ([i for i in range(n)],0);
def ansC(C):
    A = ['o' for _ in range(len(C))]; ANS = [];
    for n in C: B = A[:]; B[n] = 'x'; ANS.append(B);
    [print(k) for k in ANS];print("\n");
def isValid(C,rj):
    for ri in range(rj):
        if(C[ri] == C[rj] or abs(C[ri]-C[rj]) == rj - ri):
            return False;
    return True;
def nQ(C,m):
    if(m == len(C)): ansC(C); return;
    for i in range(m,len(C)):
        C[i],C[m] = C[m],C[i];
        if(isValid(C,m)): nQ(C,m+1);
        C[m],C[i] = C[i],C[m];
findQ(6);



























B = []

def perm(X,m,B):
    if(m == len(X)): B.append(X); return;
    for i in range(m,len(X)):
        X[i],X[m] = X[m],X[i];
        perm(X,m+1,B);
        X[i],X[m] = X[m],X[i];

A = [1,2,3,4,5]; perm(A,0,B)

