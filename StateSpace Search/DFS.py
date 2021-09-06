#Sum of subset


def ans(d,x,k):
    s = "";n = len(x)
    for i in range(n):
        if(x[i] > 0): s += str(d[i]) + "+"
    s = s[:len(s)-1]
    return s + " = " + str(k);

def add(x,e):
    d = x[:];d.append(e);
    return d

def Sum(d,x):
    s = 0;
    for i in range(len(x)):
        if(x[i] > 0): s += d[i];
    return s;

def subsetsumDFS(d,k):
    s = [];n = len(d);m = 1;
    s.append([]);
    while(len(s) > 0):
        x = s.pop();
        if (len(x) < len(d)):
            x0 = add(x,0); x1 = add(x,1)
            s.append(x1);s.append(x0);
        elif(Sum(d,x) == k): print(ans(d,x,k))

a = [1,2,3,4,5];
subsetsumDFS(a,10)

a = [2,3,4,5,6,7,8,11,25,32,56]
subsetsumDFS(a,60)


def m3d2R(n,t,s):
    if(n == t): return ""
    if(not n//2 in s):
        s.add(n//2); r = m3d2R(n//2,t,s);
        if(r != None): return "/2" + r;
    if(not n*3 in s):
        s.add(n*3); r = m3d2R(n*3,t,s);
        if(r != None): return "*3" + r;
    return None
        
    

def m3d2DFS(target):
    return "1"+ str(m3d2R(1,target,set()))+"="+str(target);



    
    
        
