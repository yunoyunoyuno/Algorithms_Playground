class minWeightHeap():
    data = []; l = 0;
    def __init__(s,d=[]):
        if(len(d) == 0): return;
        s.l = len(d); s.data = d;
        for k in range(len(d)-1,-1,-1): s.__fD(k);
    def __gt(s,i,j): return s.data[i][2] < s.data[j][2];
    def __fD(s,p):
        while(2*p + 1 < s.l):
            t = 2*p + 1;
            if(t +1 < s.l and s.__gt(t+1,t)): t += 1;
            if(s.__gt(t,p)): s.data[t],s.data[p] = s.data[p],s.data[t];
            p = t;
    def deQ(s):
        e = s.data[0]; s.data[s.l-1],s.data[0] = s.data[0],s.data[s.l-1];
        s.data.pop(); s.l -= 1; s.__fD(0);return e;
    def size(s): return s.l;
    def display(s): print(s.data);

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
    def __new__(s,V,E,t = "d"):
        E = list(set(E));
        if(len(E) > 0.4*V*(V-1)):
            return DenseGraph(V,E,t);
        return SparseGraph(V,E,t);
    def size(s): return s.size();

V = 5; E = [(1,4,5),(1,2,2),(2,4,5),(2,3,14),(2,5,4),(3,5,34),(4,5,58)]
H = minWeightHeap(E);

G = Graph(V,E,'u');
'''
H.display();
while(H.size() > 0): print(H.deQ());
'''





P = [None,11,2,2,3,7,6,7,6,6,10,2]
H = [None,None,2,None,None,None,1,1,None,None,0,None]

def findSet(e):
    if(P[e] == e): return e;
    return findSet(P[e]);

def unionSet(s,t):
    if(H[s] < H[t]): P[s] = t;
    else:
        P[t] = s;
        if(H[s] == H[t]): H[s] += 1;

a = findSet(10);
































    
