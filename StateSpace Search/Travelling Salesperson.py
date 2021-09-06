import matplotlib.pyplot as plt
import numpy as np

class minHeapD:
    data = []; l = 0;
    def size(s): return s.l;
    def gt(s,i,j): return s.data[i][1] < s.data[j][1];
    def swap(s,i,j): s.data[i],s.data[j] = s.data[j],s.data[i];
    def fU(s,k):
        while(k > 0):
            p = (k-1)//2;
            if(s.gt(k,p)): s.swap(p,k);
            k = p;
    def fD(s,p):
        while(2*p + 1 < s.l):
            c = 2*p + 1;
            if(c+1 < s.l and s.gt(c+1,c)): c += 1;
            if(s.gt(c,p)): s.swap(c,p);
            p = c;
    def enQ(s,obj):
        s.data.append(obj); s.fU(s.l); s.l += 1;
    def deQ(s):
        e = s.data[0]; s.swap(0,s.l-1);s.data.pop();
        s.l -= 1; s.fD(0); return e;
          
class Q:
    data = [None]; front = 0; l = 0;
    def size(s): return s.l;
    def __inc(s,j): return  (j+1)%len(s.data);
    def enQ(s,obj):
        if(s.l == len(s.data)):
            j = s.front;
            m = [None for _ in range(2*len(s.data))];
            for i in range(s.l): m[i] = s.data[j]; j = s.__inc(j);
            s.data = m; s.front = 0;
        j = (s.front + s.l)%len(s.data);
        s.data[j] = obj; s.l += 1;
    def deQ(s):
        e = s.data[s.front]; s.data[s.front] = None;
        s.front = s.__inc(s.front); s.l -= 1;
        return e;

class SparseGraph:
        def __init__(s,V,E,t):
            s.V = [None for i in range(V)]; s.l = V; s.t =t; s.type = "AJL"
            for e in E:
                if(len(e) > 2): s.addEdge(e[0],e[1],e[2]);
                else: s.addEdge(e[0],e[1]);         
        def __gN(s,v1,v2):
            c = s.V[v1-1];
            if(c == None): return None;
            for nbh in c:
                if(nbh[0] == v2): return nbh;
            return None;             
        def __rE(s,v1,v2):
            c = s.V[v1-1];n = s.__gN(v1,v2);
            if(c == None or n == None): return;
            c.remove(n); s.l -= 1;     
        def __aE(s,v1,v2,w=1):
            c = s.V[v1-1]; n = s.__gN(v1,v2);
            if(c == None):  s.V[v1-1] = [(v2,w)]
            elif(n == None): c.append((v2,w));
            else: n[1] = w;
        def adj(s,v): return s.V[v-1];
        def size(s): return s.l;
        def addEdge(s,v1,v2,w=1):
            if(s.t == 'u'): s.__aE(v1,v2,w); s.__aE(v2,v1,w);
            else: s.__aE(v1,v2,w)          
        def addVertex(s,n):
            for _ in range(n): s.V.append(None);
            s.l += n;
        def removeEdge(s,v1,v2):
            if(s.t == 'u'): s.__rE(v1,v2); s.__rE(v2,v1);
            else: s.__rE(v1,v2);       
        def removeVertex(s,v):
            if(v > s.l): return;
            for i in range(len(s.V)):
                if(v != i+1): s.removeEdge(i+1,v);
                else: s.V[v-1] = None;
            s.l -= 1;
        def display(s):
            for i in range(len(s.V)):
                print(i+1,s.V[i]);               
        def contains(s,v1,v2): return s.__gN(v1,v2) != None;
        
class DenseGraph:
    def __init__(s,V,E,t):
        s.V = [[0 for i in range(V)] for j in range(V)];s.l = V; s.t = t;
        s.type = "AJM";s.E = E;
        for e in E:
            if(len(e) > 2): s.addEdge(e[0],e[1],e[2]);
            else: s.addEdge(e[0],e[1]);      
    def addEdge(s,i,j,w = 1):
        if(s.t == 'u'): s.V[i-1][j-1] = w; s.V[j-1][i-1] = w;
        s.V[i-1][j-1] = w;
    def removeEdge(s,i,j):
        if(s.t == 'u'): s.V[i-1][j-1] = 0; s.V[j-1][i-1] = 0;
        s.V[i-1][j-1] = 0;
    def adVertex(s,n):
        k = [0 for _ in range(len(s.V)+n)];
        for v in s.V:
            for _ in range(n): v.append(0);
        s.V.append(k); s.l += n;
    def removeVertex(s,i):
        for k in range(len(s.V)):
            s.V[i-1][k] = 0; s.V[k][i-1] = 0;
        s.l -= 1;
    def display(s):
        for i,e in enumerate(s.V):
            print(i+1,e);
    def contains(s,v1,v2): return s.V[v1-1][v2-1] > 0;
    def adj(s,v): return s.V[v-1];
    def size(s): return s.l;

class Graph(SparseGraph):
    def __new__(s,V,E,t = "d",mode = ""):
        E = list(set(E));
        if(len(E) > 0.4*V*(V-1) or mode == "M"):
            return DenseGraph(V,E,t);
        return SparseGraph(V,E,t);
    def size(s): return s.size();

def tourLength(G,X):
    g = G.V;s = 0;
    x = X[:]; x.append(X[0]);
    for i in range(len(X)):
        if(g[x[i]-1][x[i+1]-1] == 0): return 1e6;
        s += g[x[i]-1][x[i+1]-1];
    return s;

V = 8; E= [(1,2,4),(1,3,7),(1,4,16),(2,3,5),(2,5,15),
           (2,6,10),(2,8,13),(3,4,8),(3,5,9),(4,5,2),
           (4,7,3),(5,7,1),(5,6,14),(5,8,6),(6,8,11),
           (7,8,12)]

G = Graph(V,E,"u","M");

def ans(X,V):
    s = "";
    for e in X: s += f'{e} -> ';
    s += str(X[0]);
    print("Salesman should go through",s);
    print("Using distance",V);
    
SDFS = []
#Traveling Salesman DFS
def TSPR(G,X,m,Lm,Xmin):
    if(m == G.size()):
        l = tourLength(G,X); x = X[:]; x.append(X[0]); SDFS.append(x);
        if(l < Lm[0]): 
            Lm[0] = l; Xmin[0] = X[:]; 
    else:
        for i in range(m,G.size()):
            X[m],X[i] = X[i],X[m];
            TSPR(G,X,m+1,Lm,Xmin);
            X[m],X[i] = X[i],X[m];
    
def DFSTSP(G,init):
    Lmin = [tourLength(G,init)];
    Xmin = [None];
    TSPR(G,init,1,Lmin,Xmin);
    ans(Xmin[0],Lmin[0]);
    return Xmin[0],Lmin[0];

DFSTSP(G,[1,2,3,4,5,6,7,8])



SBFS = [];
#Traveling Salesman BFS ~>_<。＼ BFSTSP(G,[1,2,3,4,5,6,7,8]);
def BFSTSP(G,init):
    Lmin = 1e6; Xmin = [None];
    q = Q(); q.enQ((init,1));
    while(q.size() > 0):
        X,m = q.deQ();
        if(G.size() == m):
            l = tourLength(G,X); x = X[:]; x.append(X[0]); SBFS.append(x);
            if(l < Lmin):
                Xmin[0] = X[:];Lmin = l;
        else:
            for i in range(m,G.size()):
                X[i],X[m] = X[m],X[i];
                X1 = X[:]
                q.enQ((X1,m+1));
                X[m],X[i] = X[i],X[m];
    ans(Xmin[0],Lmin);
    return (Xmin[0],Lmin);

BFSTSP(G,[1,2,3,4,5,6,7,8]);



#Traveling Salesman BranchAndBound ◑﹏◐ ·´¯`
#Lowerbound For B&B !!!!!!!!>▂<´¯`· !!!!!!!!!!!!!!!
def tourLengthLB(G,X,m):
    E2 = G.E[:]; v = G.size();
    G2 = Graph(v,E2,"u","M");
    [G2.removeVertex(X[i]) for i in range(m) ]; 
    g = [e[:] for e in G2.V]; v2 = len(g); s= 0;
    for i in range(m-1):
        if(G.V[X[i]-1][X[i+1] - 1] == 0): s += 1e5;
        s += G.V[X[i]-1][X[i+1] - 1];
    #print("1",s);
    for r in range(m,v):
       mn = 100;
       for c in range(m,v):
           if(g[r-1][c-1] > 0 and g[r-1][c-1] < mn): mn = g[r-1][c-1];
       if(mn < 100) : s+= mn;
    #print("2",s)
    if(G.V[X[-1]-1][0] > 0): s += G.V[X[-1]-1][0]
    else: s += 1e5;
    #print(X,m);
    #print("3",s,X)
    #G2.display();
    #G.display();
    #print("s",s)
    return s;
        
    
SBB = []
def BBTSP(G):
    H = minHeapD(); Xm = [1,4,7,5,8,6,2,3];v = G.size();
    Lm = 1e4; H.enQ((Xm,tourLengthLB(G,Xm,1),1));
    while(H.size() > 0):
        (X,Llb,m) = H.deQ();
        x = X[:]; x.append(X[0]); SBB.append(x);
        if(Llb >= Lm): break;
        if(m == v):
            Lm = Llb; Xm = X[:];
        else:
            for i in range(m,v):
                X1= X[:];
                X1[m],X1[i] = X1[i],X1[m];
                H.enQ((X1,tourLengthLB(G,X1,m+1),m+1));
    
    ans(Xm,Lm);
    return (Xm[0],Lm);


BBTSP(G);

#tourLengthLB(G,[1,2,6,8,5,7,4,3],8)

plt.ion()
O = [1,2,6,8,7,5,4,3];
x, y = [2,4,4,4,6,6,8,8],[5,8,5,2,4.6,6.5,2,8]
Y = [[x[i-1] for i in O],[y[i-1] for i in O]]
Y[0].append(x[0]); Y[1].append(y[0]);

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(Y[0], Y[1], 'b-')
ax.scatter(x,y);
plt.xlim(0,10)
plt.ylim(0,10)

for S in SBB:
    nY = [y[i-1] for i in S]; nX = [x[i-1] for i in S]
    line1.set_ydata(nY)
    line1.set_xdata(nX)
    fig.canvas.draw()
    plt.pause(0.08)


fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(Y[0], Y[1], 'b-')
ax.scatter(x,y);
plt.xlim(0,10)
plt.ylim(0,10)




#plt.waitforbuttonpress()


'''
T = [(1,3),(4,2),(5,4)]
q = Q();
for k in T: q.enQ(k);
for k in T: print(q.deQ());
q.enQ(([],4));
print(q.deQ());


D = [(4,2),(3,8),(4,3),(6,-1),(9,10)]; H = minHeapD();
for e in D: H.enQ(e);
for _ in D: print(H.deQ());

'''

'''
def perm(arr,m):
    if(m == len(arr)): print(arr); return;
    for i in range(m,len(arr)):
        arr[i],arr[m] = arr[m],arr[i];
        perm(arr,m+1);
        arr[i],arr[m] = arr[m],arr[i];
''' 

































