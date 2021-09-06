#Modest Local Search.
# NP-HARD Optimization Problem. [Not best soln, good one.]

#1 KnapSack ✔
#2 TSP ✔
#3 Playing ... ►__◄ ✔

import random;
import pandas as pd;
import matplotlib.pyplot as plt;

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

class Item:
    def __init__(s,v,w): s.v = v; s.w = w; s.cost = v/w;
    
#Easiest partition.
def partition(A,L,R):
    p = A[L].cost; i = L+1; j = R;
    while(i < j):
        while(i < R and p < A[i].cost): i += 1;
        while(A[j].cost <= p): j -= 1;
        if(i < j): A[i],A[j] = A[j],A[i];
    if(p < A[j].cost): A[j],A[L] = A[L],A[j];
    return j

def qS(A,L,R):
    if(L < R): j = partition(A,L,R); qS(A,L,j-1);qS(A,j+1,R);
    
def quickSortItems(A): qS(A,0,len(A)-1);

Items = [(5,20), (7,21), (10,5)];
Items = [Item(e[0],e[1]) for e in Items];

#quickSortItems(Items);

def S(v,x):
    s= 0;
    for i in range(len(v)): s += v[i]*x[i];
    return s;

# HillClimbing o:><；oo
def knapsack(w,v,W):
    maxV = 0;
    maxX = [0 for _ in range(len(v))];
    good = True;
    while(good):
        x = maxX; good = False;
        for i in range(len(v)):
            x[i] = 1 - x[i]; sumv = S(v,x);
            if(S(w,x) <= W and sumv > maxV):
                maxX = x[:]; maxV = sumv; good = True;
                break #;( Simple)
            x[i] = 1 - x[i]
    return maxX;

v = [10,30,40,5,12];
w = [25,34,41,22,60];
X = knapsack(w,v,100);



#[ print(e.v,e.w,e.cost) for e in Items ];
'''
Soon.～.눈_눈
V(i,j) = max{V(i-1,j),vi + V(i,j - wi)}; wi >= j, i > 0
         V(i-1,j);                       wi < j
         0  ;                            i ==0 or j ==0 


'''
'''
def localSearch(p):
    s = initalSln(p);
    while(not terminate(p,s)):
     s2 = select nbh(p,s);
     if( accept(p,s,s2)): s = s2;
'''
    
#TSP;

V = 8; E= [(1,2,4),(1,3,7),(1,4,16),(2,3,5),(2,5,15),
           (2,6,10),(2,8,13),(3,4,8),(3,5,9),(4,5,2),
           (4,7,3),(5,7,1),(5,6,14),(5,8,6),(6,8,11),
           (7,8,12)]

G = Graph(V,E,"u","M");

#Fisher–Yates shuffle ● ◡ ● 
def shuffle(A):
    for i in range(len(A)-1,0,-1):
        j = random.randint(1,i); A[i],A[j] = A[j],A[i];

# TSP Hill Climbing ˘︹˘

def tourLength(M,X):
    g = M; v = len(M);
    if(g[X[0]][X[-1]] == 0): return 1e6;
    #print(g[X[0]][X[-1]])
    s= g[X[0]][X[-1]]
    for i in range(len(X)-1):
          if(g[X[i]][X[i+1]] == 0): return 1e6;
          s += g[X[i]][X[i+1]];
    return s;


def tsp(M):
    n = len(M);minT = [i for i in range(n)];
    d = []; minL = [tourLength(M,minT)];
    for i in range(1500):
        shuffle(minT);
        goodAns = True;
        while(goodAns):
            X = minT; goodAns = False;
            for i in range(1,n-1):
                for j in range(i+1,n):
                    X[i],X[j] = X[j],X[i];
                    length = tourLength(M,X);
                    if(length < minL[0]):
                        x = X[:];x.append(x[0]);d.append(x);
                        minL[0] = length; minT = X[:]; goodAns = True;
                        #break;
                    X[i],X[j] = X[j],X[i];
    return (minL,d)

#tsp(G);
df = pd.read_csv("th.csv");

#print(df);
cap = df[(df.capital == 'primary') | (df.capital == 'admin')];

latlng = cap[["lat","lng"]].values.tolist();
plt.ion()
O = [i for i in range(77)];
M = [ [0 for i in range(77)] for j in range(77)];

for r in range(len(M)):
    for c in range(len(M)):
        v = random.random()
        if(v > 0.1): M[r][c] = v*100;


O = [i for i in range(77)];
x, y = cap["lat"].values.tolist(),cap["lng"].values.tolist()
Y = [[x[i] for i in O],[y[i] for i in O]]
Y[0].append(x[0]); Y[1].append(y[0]);
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(Y[0], Y[1], 'b-')
ax.scatter(x,y);

mL,D = tsp(M);

for S in D:
    nY = [y[i] for i in S]; nX = [x[i] for i in S]
    line1.set_ydata(nY)
    line1.set_xdata(nX)
    fig.canvas.draw()
    plt.pause(0.02)
    
print("Upper bound Distance",mL[0]);

#plt.xlim(0,10)
#plt.ylim(0,10)

'''
def swap(A):
    A2 = A[:]
    for i in range(1,len(A)-1):
        for j in range(i+1,len(A)):
            A[i],A[j] = A[j],A[i];
            print(A)
        A = A2[:];
'''

#A = [1,2,3,4]; shuffle(A); print("s",A);
#swap(A);
'''

'''



















































