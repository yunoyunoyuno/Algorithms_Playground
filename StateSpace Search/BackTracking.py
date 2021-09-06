#Sum of subset backtracking.

def Sum(d,x):
    s = 0;
    for i in range(len(x)): s += d[i]*x[i];
    return s;

def ans(d,x,k):
    s = "";
    for i in range(len(x)-1):
        if(x[i] > 0): s += str(d[i]) + "+";
    if(x[-1] == 1): s += str(d[i])
    print(s,"=",k)
    

#DFS

def subsetsumR(d,k,x,m):
    s = Sum(d,x);
    if(s > k): return;
    if(m == len(x)-1):
        if(s == k): ans(d,x,k);
    else:
        x[m+1] = 1; subsetsumR(d,k,x,m+1);
        x[m+1] = 0; subsetsumR(d,k,x,m+1);

def subsetsumDFSB(d,k):
    n = len(d); x = [0 for i in range(n)];
    return subsetsumR(d,k,x,0);

def add(x,n):
    x = x[:];
    x.append(n);
    return x

def subsetsumBFSB(d,k):
    q = [];
    x = [0];
    q.append(x);
    while(len(q) > 0):
        x = q.pop(0);
        s = Sum(d,x)
        if( s <= k):
            if(len(x) == len(d)):
                if(s == k): ans(d,x,k)
            else:
                x0 = add(x,0);x1 = add(x,1);
                q.append(x0); q.append(x1);

d = [2,3,4,5,1,10,16,21];
subsetsumDFSB(d,40);
subsetsumBFSB(d,40);
