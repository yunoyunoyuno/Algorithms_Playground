#Review
def inc(x):
    i = len(x) -1
    while(i >= 0):
        if(x[i] == 0): break;
        x[i] = 0; i-= 1;
    if(i >= 0): x[i] = 1;
    print(x);

def b_counter(n):
    x = [1 for _ in range(n)];
    for i in range(2**n): inc(x)


def bcounter2(n):
    x = [0 for i in range(n)];
    counter(x,0);

def counter(x,m):
    if(m >= len(x)): print(x); return;
    x[m] = 1; counter(x,m+1);
    x[m] = 0; counter(x,m+1);


#b_counter(4);
#bcounter2(4);

'''
def eR(x,m):
    print(x);
    for i in range(x[m] + 1,len(x)):
        x[m+1] = i; eR(x,m+1);

def enumSubSet(n):
    x = [0 for _ in range(n)];
    eR(x,0);

enumSubSet(5);
'''

def bR(x,m):
    if(m == len(x)): print(x); return;
    x[m] = 1; bR(x,m+1);
    x[m] = 0; bR(x,m+1);
    
def bcounter2(n):
    x = [0 for i in range(n)];
    bR(x,0);


#bcounter2(3);

def S(x,d):
    s = 0;
    for i in range(len(x)): s+= x[i]*d[i];
    return s;

def add(x,n):
    x = x[:]; x.append(n);
    return x;

def show(x,d,k):
    s = "";print(d);
    for i in range(len(x)-1):
        if(x[i] > 0): s += f'{d[i]} + '
    if(x[-1] > 0): s += f'{d[len(x)-1]} = {k}'
    print(s);
    
def sumofsubset(d,k):
    x = [];
    stack = [x];
    while(len(stack) > 0):
        x = stack.pop();
        if(S(x,d) == k ): show(x,d,k); return x;
        if(len(x) < len(d)):
            j = len(x);
            if(j < len(d) and S(x,d) + d[j] <= k): x1 = add(x,1); stack.append(x1);
            x0 = add(x,0); stack.append(x0);


#a = sumofsubset([1,3,4,5,6,7,3,4,6,11,23,25,34,22,13,45,10,23,21,-2],149);    
    

def queenState(a,m):
    if(m == len(a)): print(a); return;
    for i in range(len(a)):
        a[m] = i; queenState(a,m+1);

a = [0 for _ in range(3)]; #queenState(a,0);

#N-Queen
def ans(c):
    n = len(c);
    for e in c:
        if(e == None): continue;
        k = ['o' for _ in range(n)]; k[e] = 'x'; print(k);
    print("\n");

def queen(c,m):
    if(m == len(c)): ans(c);return;
    for i in range(len(c)):
        c[m] = i;
        if(isValid(c,m)): queen(c,m+1);

def isValid(c,k):
    r1 = k;
    for r2 in range(r1):
        if(c[r1] == c[r2] or abs(c[r1] - c[r2]) == abs(r1 - r2)): return False
    return True;

def findQueen(n):
    print(n,"Queen\n");
    c = [0 for _ in range(n)]; queen(c,0);

#findQueen(4);


#0/1 Knapsack Backtracking;

def S(M,N):
    s = 0;
    for i in range(len(W)): s+=M[i]*N[i];
    return s;
def kans(X,V,W,Vm,w):
    ANS = [];print("There are",len(V),"items in",w,"kg. bag");
    for i in range(len(V)):
        print(i+1,"Value : ",V[i],"Weight",W[i]);
        if(X[i] > 0): ANS.append((i+1,V[i],W[i]));
    [print("Put item",e[0],"Value",e[1],"Weight",e[2],"in this bag") for e in ANS];
    print("You will get maximum value of",Vm[0]);

def kR(X,V,W,w,m,Xm,Vm):
    if(S(X,W) > w): return;
    if(m == len(V)):
        if(S(V,X) > Vm[0]): Vm[0] = S(V,X); Xm.append(X[:]);
    else:
        X[m] = 1;kR(X,V,W,w,m+1,Xm,Vm);
        X[m] = 0;kR(X,V,W,w,m+1,Xm,Vm);

def knapSack(V,W,w):
    X = [0 for _ in range(len(V))];
    Xm = []; Vm = [-1e6];A =[];
    kR(X,V,W,w,0,Xm,Vm);
    kans(Xm[-1],V,W,Vm,w);

V = [10,30,40,20,43,65]; W = [2,10,12,30,4,21];
#knapSack(V,W,100);

def perm(a,m):
    if(m == len(a)-1): print(a); return;
    for i in range(m,len(a)):
        a[i],a[m] = a[m],a[i];
        perm(a,m+1);
        a[i],a[m] = a[m],a[i];

A = [1,2,3];
perm(A,0);



























    
