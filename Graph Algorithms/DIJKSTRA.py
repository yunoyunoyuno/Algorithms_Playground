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

class minHeapD:
    l = 0; data = [];
    def __init__(s,d = []):
        if(len(d) == 0): return;
        s.l = len(d); s.data = d[:];
        for i in range(s.l-1,-1,-1): s.__fixD(i);
    def __gt(s,i,j): return s.data[i][1] <= s.data[j][1];
    def __fixD(s,p):
        while(2*p + 1 < s.l):
            t = 2*p + 1;
            if(t+1 < s.l and s.__gt(t+1,t)): t += 1;
            if(s.__gt(t,p)): s.data[t],s.data[p] = s.data[p],s.data[t];
            p = t;
    def __fixU(s,k):
        while(k > 0):
            t = (k-1)//2;
            if(s.__gt(k,t)): s.data[t],s.data[k] = s.data[k],s.data[t];
            k = t;
    def deQ(s):
        if(s.size() == 0): return;
        e = s.data[0]; s.data[s.l-1],s.data[0] = s.data[0],s.data[s.l-1];
        s.data.pop(); s.l -= 1; s.__fixD(0); return e;
    def size(s): return s.l;
    def edit(s,k,v):
        for i in range(s.l):
            if(s.data[i][0] == k):
                s.data[i][1] = v; s.__fixU(i);
    def toArray(s): return s.data[:];

E = [(1,2,2),(1,4,1),(2,4,3),(2,5,10),(3,1,4),(3,6,5),
     (4,6,8),(4,3,2),(4,7,4),(4,5,2),(5,7,6),(7,6,1)]
V = 7;GD = Graph(V,E,'d'); GU = Graph(V,E,'u');

def dijkstra(G,s):
    if(G.adj(s) == None): return s;
    v = G.size(); si = s-1; P = [None for _ in range(v)];
    D = [[i+1,1e6] for i in range(v)]; D[si][1] = 0;
    H = minHeapD(D);
    while(H.size() > 0):
        u = H.deQ(); ui = u[0]; du = u[1];
        if(G.adj(ui) == None): continue;
        for v in G.adj(ui):
            vi = v[0]; wuv = v[1]; vdi = vi -1;dv = D[vdi][1];
            if(du + wuv < dv):
                D[vdi][1] = du + wuv; P[vdi] = ui; H.edit(vi,D[vdi][1]);
    print("\nGraph is\n");G.display(); show = [];
    for i,d in enumerate(P):
        k = ""
        while(d != None): k = f'{d} -> ' + k; d = P[d-1];
        k += f'{i+1}'; show.append(k);
    print("\n\nShortest Path from",s,"is"); [print(e) for e in show];

def prims(G):
    if(G.type == "AJL"):
        v = G.size(); P = [None for i in range(v)];
        D = [[i+1,1e6] for i in range(v)]; D[-1][1] = 0;
        H = minHeapD(D);inMST = [False for i in range(v+1)];
        while(H.size() > 0):
            u = H.deQ(); ui = u[0]; du = u[1]; inMST[ui] = True
            for v in G.adj(ui):
                vi = v[0]; wuv = v[1]; vj = vi-1; 
                if(not inMST[vi] and wuv < D[vj][1]):
                    D[vj][1] = wuv; H.edit(vi,wuv);P[vj] = ui
        print("\nGraph is\n");G.display(); show = [];
        for i,d in enumerate(P):
            if(i+1 < G.size()):show.append(f'{d} -> {i+1}');
        print("\n\nParent For Each Node Are");
        show.append(G.size());[print(e) for e in show];
        d = sum([a[1] for a in D]); 
        print("Can form MST with min length is",d);
    if(G.type == "AJM"):
        v = G.size(); P = [None for i in range(v)];
        D = [1e6 for i in range(v)]; D[-1] = 0;
        inMST = [False for i in range(v)];M = G.V[:]; mn = 0;
        for i in range(v):
            u = D.index(min(D)); mn += min(D); D[u] = 1e6; inMST[u] = True
            for j in range(v):
                if(M[u][j] > 0 and M[u][j] < D[j] and not inMST[j]):
                    D[j] = M[u][j]; P[j] = u + 1;
        print("\nGraph is\n");G.display(); show = [];
        for i,d in enumerate(P):
            if(i+1 < G.size()):show.append(f'{d} -> {i+1}');
        print("\n\nParent For Each Node Are",P);
        show.append(G.size());[print(e) for e in show];
        print("Can form MST with min length is",mn);
            
        

#dijkstra(GD,2);
prims(GU);
    



















    

'''
WD = [(1,21),(5,-1),(0,12),(9,0)];
H = minHeapD(WD);
for _ in range(H.size()):
    print(H.deQ());


'''

