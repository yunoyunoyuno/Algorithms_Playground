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

#(mn,mx) = min_max(A);
#print(mn,mx)

#Find Min and Max from an integer of an array.
def mmR2(A,R):
    if(R == 0): return (A[R],A[R]) ; 
    min1 = min(A[R],A[R-1]); max1 = max(A[R],A[R-1]);
    if(R > 1):
        (min2,max2) = mmR2(A,R-2)
        min1 = min(min1,min2); max1 = max(max1,max2);
    return (min1,max1);
    
def min_max2(A): return mmR2(A,len(A)-1);

A = [-1,-2,-3,-4,-5]

(mn2,mx2) = min_max2(A)
print("min :",mn2,"max: ",mx2)








