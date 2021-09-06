class SparseGraph:
        def __init__(s,V,E,t):
            s.V = [None for i in range(V)]; s.l = V; s.t =t;
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

'***********'
def isDAGR(u,G,C):
    C[u] = 'G';
    if(G.adj(u) != None):
        for v in G.adj(u):
            vi = v[0];
            if(C[vi] == 'G'): return False;
            if(C[vi] == 'W'):
                if(not isDAGR(vi,G,C)): return False;
    C[u] = 'B'; return True;

def isDAG(G):
    C = ['W' for i in range(G.size() + 1)];
    for i in range(1,G.size() + 1):
            if(C[i] == 'W'):
                if(not isDAGR(i,G,C)): return False;
    return True
    
def tsort(G,C,S,u):
    C[u] = 'G';
    if(G.adj(u)):
        for v in G.adj(u):
            v = v[0];
            if(v == 'W'): tsort(G,C,S,v);
    C[u] = 'B'; S.append(u);

def topologicalSort(G):
    imDAG = isDAG(G);
    if(not imDAG): return "This is only for DAG";
    S = []; C = ['W' for _ in range(G.size() + 1)];
    for u in range(1,G.size() + 1):
        if(C[u] == 'W'): tsort(G,C,S,u);
    return S;
    
V = 7; E = [(1,2),(1,3),(2,6),(3,4),(2,3),(7,2),(7,6),(6,5),(6,4)]
G = Graph(V,E,'d');G.display();

b = isDAG(G);
t = topologicalSort(G);









    
    
