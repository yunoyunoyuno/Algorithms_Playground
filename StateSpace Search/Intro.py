#Sum of subsets

def inc(x):
    n = len(x); i = n-1;
    while(i >= 0 and x[i] == 1):
        x[i] = 0; i -= 1;
    if(i >= 0 ): x[i] = 1;

def S(d=[],x=[]):
    n = len(x); s = 0;
    for i in range(n): s += d[i]*x[i];
    return s;
    

def bcounter(n):
    x = [0 for i in range(n)];
    for i in range(2**n):
        inc(x);
        print(x);

def ans(d,x):
    s = ""
    for i in range(len(x)):
        if(x[i] == 1): s += str(d[i]) + " "
    print(s);
    
def ans2(d,x,m):
    s = ""
    for i in range(1,m+1):
        s += str(d[x[i]-1]) + " "
    print(s);

def subsetSum1(d,k):
    n = len(d); x = [0 for i in range(n)];
    for i in range(2**n):
        if(S(d,x) == k): ans(d,x);
        inc(x);
def subsetSumR(d=[],x=[],k=9997,m=0):
    n = len(d);
    if(m == n):
        if(S(d,x) == k) : ans(d,x);
    else:
        x[m] = 0;subsetSumR(d,x,k,m+1);
        x[m] = 1;subsetSumR(d,x,k,m+1);
    
def subsetSum2(d,k):
    n = len(d); x = [0 for i in range(n)];
    subsetSumR(d,x,k,0);

def enumR(x,m):
    print(x[0:m+1]); n = len(x);
    for i in range(x[m]+1,n):
        x[m+1] = i; enumR(x,m+1);

def enumSubSet(n):
    x = [None]*(n+1);
    x[0] = 0;
    enumR(x,0);

def S2(d,x,m):
    s = 0;
    for i in range(1,m+1):
        s += d[x[i]-1];
    return s
        
def subSetR3(d,k,x,m):
    n = len(x);
    if(S2(d,x,m) == k): ans2(d,x,m);
    for i in range(x[m]+1,n):
        x[m+1] = i;
        subSetR3(d,k,x,m+1);
    

def subsetSum3(d,k):
    n = len(d); x = [None]*(n+1);
    x[0] = 0;
    subSetR3(d,k,x,0);
    
    


#a = [1,2,3,4,5]
#subsetSum1(a,10)
#subsetSum2(a,10)
#enumSubSet(3)   
