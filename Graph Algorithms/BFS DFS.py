class Q:
    front = 0; data = [None]; s = 0;
    def __inc(s,i): return (i+1)%len(s.data);
    def enqueue(this,obj):
        if(this.s == len(this.data)):
            m = [None]* 2*len(this.data); j = this.front;
            for i in range(this.s):
                m[i] = this.data[j]; j = this.__inc(j);
            this.data = m; this.front = 0;
        j = (this.front + this.s)%len(this.data); this.data[j] = obj; this.s += 1;
    def dequeue(this):
        e = this.peek(); this.data[this.front] = None;
        this.front = this.__inc(this.front); this.s -= 1;
        return e;
    def peek(t): return t.data[t.front];
    def size(t): return t.s;
        
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


def BFS(G):
    V = G.size(); C = ['W' for _ in range(V+1)];p = [];
    q = Q(); q.enqueue(1); C[1] = 'G'
    while(q.size() > 0):
        u = q.dequeue(); C[u] = 'B'; p.append(u);
        if(G.adj(u) != None):
            for v in G.adj(u):
                v = v[0];
                if(C[v] == 'W'):
                    q.enqueue(v); C[v] = 'G'
    print("BFS",p); print(C);
    
def ShortestPath(G,s,t):
    V = G.size(); p = [None for _ in range(V+1)]; d = [None for _ in range(V+1)];
    q = Q(); q.enqueue(s); d[s] = 0;
    while(q.size() > 0):
        u = q.dequeue();
        if(G.adj(u) != None):
            for v in G.adj(u):
                v = v[0];
                if(d[v] == None):
                    q.enqueue(v); d[v] = d[u] + 1; p[v] = u;
    print("shortest path from",s,"to",t,"is",d[t]);
    
def DFSR(u,G,C,A,P):
    if(G.adj(u) != None):
        P[u] = u;
        for v in G.adj(u):
            v = v[0];
            if(C[v] == 'W'): C[v] = 'G'; A.append(v); P[v] = u; DFSR(v,G,C,A,P);
        C[u] = 'B'
    
def DFST(G):
    A = [1]; C = ['W' for _ in range(G.size() + 1)]; C[1] = 'G';
    P = [None for _ in range(G.size() + 1)]; P[1] = 1;
    for i in range(1,G.size() + 1):
        if(C[i] == 'W'):  DFSR(i,G,C,A,P);
    print("DFSTree",P,"#P[k] = k means # of DFS tree(s)");
    
def DFS(G,u):
    A = [u]; C = ['W' for _ in range(G.size() + 1)]; C[u] = 'G';
    P = [None for _ in range(G.size() + 1)]
    DFSR(u,G,C,A,P);
    print("DFS",A);
                
        
V = 9; E = [(1,2),(1,3),(2,4),(2,5),(3,5),(4,6),(6,5),(7,1),(7,8),(8,9),(9,3)]
G = Graph(V,E,'d');G.display();
BFS(G);
DFS(G,1);
DFST(G);
ShortestPath(G,1,4);
'''
A = [1,2,3,4,5];q = Q();
for a in A: q.enqueue(a);
q.dequeue(),q.dequeue();
A = [6,7,8,9,10]
for a in A: q.enqueue(a);
while(q.size() > 0):
    print(q.dequeue())
'''
    
    
    