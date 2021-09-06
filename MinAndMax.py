#Find Min and Max from an integer of an array.


def mmR(A,L,R):
    if(R - L == 0): return (A[L],A[R]);
    if(R - L == 1):
        if(A[R] - A[L] < 0): return (A[R],A[L]);
        return (A[L],A[R]);
    mid = (L+R)//2;
    (min1,max1) = mmR(A,L,mid);
    (min2,max2) = mmR(A,mid+1,R);
    return (min(min1,min2),max(max1,max2));

def min_max(A):
    return mmR(A,0,len(A)-1);

A = [5,3,2,4,0,-1,10]

(mn,mx) = min_max(A);
