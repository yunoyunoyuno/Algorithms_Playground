A = [5,4,3,2]

def partition(A,L,R,ANS):
    i = L + 1; p = A[L]; j = R;
    while(i < j):
        A[i],A[j] = A[j],A[i]; ANS.append(A);
        while(i <= R and A[i] < p): i+= 1;
        while(A[j] > p): j -= 1;
        if(i < j): A[i],A[j] = A[j],A[i]; ANS.append(A);
    if(p > A[j]): A[L],A[j] = A[j],A[L]; ANS.append(A);

ANS = []
partition(A,0,len(A)-1,ANS);
