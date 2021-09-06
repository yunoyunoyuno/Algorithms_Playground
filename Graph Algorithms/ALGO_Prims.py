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

class minHeapWeight:
    l = 0; data = [];
    def __init__(s,data=[]):
        if(len(data) > 0):
            s.data = data; s.l = len(data);
            for i in range(len(data)-1,-1,-1): s.__fD(i);         
    def __gt(s,i,j): return s.data[i][1] < s.data[j][1];
    def __fD(s,k):
        while(2*k+1 < s.l):
            t = 2*k + 1;
            if(t+1 < s.l and s.__gt(t+1,t)): t += 1;
            if(s.__gt(t,k)): s.data[t],s.data[k] = s.data[k],s.data[t];
            k = t;
    def __fU(s,k):
        while(k > 0):
            p = (k - 1) // 2;
            if(s.__gt(p,k)): break
            s.data[p],s.data[k] = s.data[k],s.data[p];
            k = p;
    def size(s): return s.l;
    def enQ(s,obj):
        s.ensureCap(s.l+1); s.data[s.l] = obj; s.__fU(s.l); s.l += 1;   
    def ensureCap(s,n):
        m = s.data;
        if(len(s.data) <= n):
            m = [None]*(s.l+1) * 2;
            for i in range(s.l+1): m[i] = s.data[i];
            s.data = m;
    def deQ(s):
        e = s.data[s.l-1]; e,s.data[0] = s.data[0],e;
        s.data[s.l-1] = None; s.l -= 1; s.__fD(0); return e;
    def toArray(s): return [s.data[i] for i in range(s.l)];
    def decreaseW(s,k,v):
        for i in range(s.l):
            if(s.data[i][0] == k): s.data[i][1] = v; s.__fU(i); break;

def PrimsMST(G):
    v = G.size(); P = [None for _ in range(v)];
    if(G.type == "AJM"):
        D = [1e5 for _ in range(v)]; D[-1] = 0;G.display();
        G = G.V[:]; inMST = [False for _ in range(v)];
        for i in range(v):
            u = D.index(min(D)); D[u] = 1e5; inMST[u] = True;
            for vi in range(v):
                if(not inMST[vi] and G[u][vi] > 0 and G[u][vi] < D[vi]):
                    D[vi] = G[u][vi]; P[vi] = u + 1
        print("MST :",P);
    else:
        D = [[i,1e6] for i in range(1,v+1)]; D[-1] = (v,0); G.display();
        H = minHeapWeight(D[:]); inMST = [False for _ in range(v + 1)];
        while(H.size() > 0):
            u = H.deQ(); ui = u[0]; inMST[ui] = True;
            for v in G.adj(ui):
                vi = v[0]; wi = v[1];
                if(not inMST[vi] and wi < D[vi-1][1]):
                    D[vi-1][1] = wi; H.decreaseW(vi,wi); P[vi-1] = ui
        print("MST :",P);
    
    
                    

V = 7; E = [(1,2,2),(1,4,1),(2,4,3),(2,5,10),(3,1,4),(3,6,5),
     (4,6,8),(4,3,2),(4,7,4),(4,5,2),(5,7,6),(7,6,1)]
G = Graph(V,E,'u');
p = PrimsMST(G);

'''
A= [(3,2),(1,6)]; H = minHeapWeight(A);
T2 =[(5, 1), (5, 1), (4, 1), (2, 1), (2, 2), (1, 1), (2, 5), (4, 3), (3, 5), (1, 2), (3, 3), (4, 1), (5, 6), (2, 6)];
H2  = minHeapWeight(T2);

while(H2.size() > 0):
    print(H2.deQ());

'''





















'''
A =  [4,2,3,1];
h = minHeap(A)
while(h.size() > 0):
    print(h.deQ());
'''
            
            
            
            
            
            
