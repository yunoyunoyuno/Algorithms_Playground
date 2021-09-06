def powermod(a,k,m):
    if(k==0): return 1;
    p = powermod(a,k//2,m);
    if(p % 2 == 0): return (p**2)%m;
    return a*(p**2)%m;


a = powermod(2,60,10)
