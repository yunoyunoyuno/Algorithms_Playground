# Normal
def fib(n):
    if(n < 2): return n;
    return fib(n-1) + fib(n-2)

# Top down

def Fib2(n,F):
    if(n < 2): return n;
    if(F[n-1] != None): return F[n-1];
    F[n-1] = Fib2(n-2,F)+ Fib2(n-1,F)
    return F[n-1];
def fib2(n):
    FIB = [None] * n; return Fib2(n,FIB)

# Bottom Up;
def fib3(n):
    f0 = 0; f1 = 1; f2 = 0;
    for i in range(n-1):
        f2 = f1+f0;
        f0 = f1; f1 = f2;
    return f1 if n == 1 else f2;

n = 34;
f = fib2(n); print("Top down Fibonacci Finder is complete !!!",f);
f2 = fib3(n); print("Bottom Up Fibonacci Finder is complete !!!",f2);
f1 = fib(n); print("Normal Fibonacci Finder is complete !!!",f1);


    
    
    
    