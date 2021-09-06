class Q:
    front = 0;data = [None]; l = 0;
    def __inc(s,j): return (j+1)%len(s.data);
    def enqueue(s,obj):
        if(len(s.data) == s.l):
            m = [None] * 2*len(s.data); j = s.front;
            for i in range(s.l):
                m[i] = s.data[j]; j = s.__inc(j);
            s.data = m; s.front = 0;
        j = (s.l + s.front)%len(s.data); s.data[j] = obj;s.l += 1;
    def peek(s): return s.data[s.front];
    def dequeue(s):
        e = s.peek();s.data[s.front] = None; s.front = s.__inc(s.front); s.l -= 1;
        return e;
    def size(s): return s.l;

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
        E = list(set(E));s.E = E;
        if(len(E) > 0.4*V*(V-1)): return DenseGraph(V,E,t);
        return SparseGraph(V,E,t);
    def size(s): return s.size();
    
def dfsR(G,C,u,A,P):
    C[u] = 'G';
    if(G.adj(u)):
        for v in G.adj(u):
            v = v[0];
            if(C[v] == 'W'): A.append(v);P[v-1] = u; dfsR(G,C,v,A,P); A.append(u);
    C[u] = 'B';
    
def DFST(G):
    v = G.size(); C = ['W' for _ in range(v+1)];
    A = []; P = [None for _ in range(v)];
    for i in range(1,v+1):
        if(C[i] == 'W'): A.append(i); dfsR(G,C,i,A,P);
    print(A);print(P);
    
def partition(A,L,R):
    p = A[L][1]; i = L+1; j = R;
    while(i < j):
        while(A[i][1] >= p): i += 1;
        while(A[j][1] < p): j -= 1;
        if(i < j): A[i],A[j] = A[j],A[i];
    if(p < A[j][1]): A[L],A[j] = A[j],A[L];
    return j;
    
def qS(A,L,R):
    if(L < R):
        mid = (L + R)//2;
        j = partition(A,L,R);
        qS(A,L,mid);
        qS(A,mid+1,R);
def quickSort(A):
    qS(A,0,len(A)-1);
    
def dfsR2(G,C,D,F,u,t):
    C[u] = 'G';D[u] = t[0] + 1; t[0] = t[0] + 1;
    if(G.adj(u)):
        for v in G.adj(u):
            v = v[0];
            if(C[v] == 'W'): dfsR2(G,C,D,F,v,t);
    C[u] = 'B'; F[u] = t[0] + 1; t[0] = t[0] + 1;
    
def TPS(G):
    v = G.size(); D = [0 for _ in range(v+1)]; F = [0 for _ in range(v+1)];
    C = ['W' for _ in range(v+1)]; time = [0];
    for i in range(1,v+1):
        if(C[i] == 'W'): dfsR2(G,C,D,F,i,time);
    print("DFS TIME IN-OUT");
    print(C);print(D); print(F);
    
def dfsSCC1(G,C,F,t,u):
    C[u] = 'G'; t[0] += 1;
    if(G.adj(u)):
        for v in G.adj(u):
            v = v[0];
            if(C[v] == 'W'): dfsSCC1(G,C,F,t,v);
    C[u] = 'B'; F[u] = t[0] + 1; t[0] += 1;

def dfsSCC2(G,C,P,u):
    C[u] = 'G';
    if(G.adj(u)):
        for v in G.adj(u):
            v = v[0];
            if(C[v] == 'W'): P[v-1] = v;dfsSCC2(G,C,P,v);
    C[u] = 'B';
            
def findSCC(G,E):
    v = G.size(); P = [None for _ in range(v)]; C = ['W' for _ in range(v+1)];
    F = [0 for _ in range(v+1)]; t = [0]; ET = [(e[1],e[0]) for e in E];
    G2 = Graph(v,ET);
    for i in range(1,v+1):
        if(C[i] == 'W'): dfsSCC1(G2,C,F,t,i);
    F = [(i,F[i]) for i in range(1,len(F))];
    quickSort(F); C = ['W' for _ in range(v+1)];
    s = "";
    for e in F:
        vi = e[0];
        if(C[vi] == 'W'): dfsSCC2(G,C,P,vi);
    for i in range(len(P)):
        if(P[i] == None): s += f" Head({i+1})"
        else: s += f'->{i+1}'
    print(s);


V = 5; E = [(1,2),(1,3),(3,2),(3,5),(4,3),(4,2),(5,4)]; #ET = [(e[1],e[0]) for e in E];
VS = 8; ES = [(1,2),(2,3),(3,4),(4,1),(3,5),(5,6),(6,7),(7,5),(7,8)]; 

G = Graph(V,E);
#G.display();
#DFST(G);
#TPS(G);

G2 = Graph(VS,ES);
findSCC(G2,ES);
'''
GT = Graph(V,ET);
GT.display();
'''
'''
A = [1,2,3,4,5];q = Q();
for a in A: q.enqueue(a);
q.dequeue(),q.dequeue();
A = [6,7,8,9,10]
for a in A: q.enqueue(a);
while(q.size() > 0):
    print(q.dequeue())    
'''    
    
    