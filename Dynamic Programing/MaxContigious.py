import random;

def P(A,n):
    if(n == 0): return A[0];
    return max(P(A,n-1) + A[n],A[n]);

def S(A,n):
    if(n == 0): return A[0];
    p = P(A,n);
    return max(S(A,n-1),p);

def sbtu_fat(A):
    P = [0 for _ in range(len(A))];
    S = [0 for _ in range(len(A))];
    P[0] = A[0]; S[0] = A[0]; n = len(A)
    for i in range(1,n):
        P[i] = max(P[i-1] + A[i],A[i]);
    for i in range(1,n):
        S[i] = max(S[i-1],P[i]);
    return S[n-1];

def find_maxContigous(A):
    P = A[0]; S = A[0]; ans = []
    for i in range(1,len(A)):
        P = max(P + A[i],A[i]); OS = S; S = max(S,P);
        print(P,OS,S);
        if(OS <= S and P > OS): ans.append(A[i]);
    print("INPUT\n",A);
    return print(ans,"whose summation is",S);

A = [-2,7,6,-3,5]; ans = find_maxContigous(A);