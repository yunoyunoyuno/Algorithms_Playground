def perm(A,m):
    if(m == len(A)): print(A); return;
    for i in range(m,len(A)):
        A[i],A[m] = A[m],A[i];
        perm(A,m+1);
        A[i],A[m] = A[m],A[i];

A = [1,2,3];

perm(A,0);
