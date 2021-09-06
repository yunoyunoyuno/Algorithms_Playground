class SparseGraph:
    class Vertex:
        def __init__(s,v,n,w = 1): s.v = v; s.n = n; s.w = w;
    def __init__(s,V,E,t = "d"):
        s.V = [None for _ in range(V)]; s.t = t; s.l = V;
        if(t == "u"):
            for e in E:
                if(len(e) > 2): s.putEdge(e[0],e[1],e[2]);s.putEdge(e[1],e[0],e[2]);
                else: s.putEdge(e[0],e[1]); s.putEdge(e[1],e[0]);
        else:
            for e in E:
                if(len(e) > 2): s.putEdge(e[0],e[1],e[2]);
                else: s.putEdge(e[0],e[1]);
                
    def size(s): return s.l
    def getNode(s,i,j):
        cur = s.V[i-1];
        while(cur != None and cur.v != j): cur = cur.n;
        return cur;
    
    def contains(s,v1,v2): return s.getNode(v1,v2) != None;
    def addVertex(s,n):
        for i in range(n): s.V.append(None); s.l += 1;
    
    def toArray(s,v):
        vertices = []; c = s.V[v-1];
        while(c != None): vertices.append((c.v,c.w)); c = c.n;
        return vertices if len(vertices) > 0 else None
    
    def putEdge(s,v1,v2,w = 1):
        if(s.t == "u"): s.__pE(v1,v2,w); s.__pE(v2,v1,w);
        else: s.__pE(v1,v2,w);
    
    def __pE(s,v1,v2,w):
        n2 = s.getNode(v1,v2); n1 = s.V[v1-1];
        if(n2 == None): n1 = s.Vertex(v2,n1,w); s.V[v1-1] = n1;
        else: n2.w = w;
        
    def __rE(s,v1,v2):
        n2 = s.getNode(v1,v2);
        if(n2 == None): return;
        if(n2 == s.V[v1-1]): s.V[v1-1] = n2.n;
        else:
            p = s.V[v1-1]; c = s.V[v1-1].n;
            while(c != n2): c = c.n; p = p.n;
            p.n = c.n;
    def removeEdge(s,v1,v2):
        if(s.t == 'u'): s.__rE(v1,v2); s.__rE(v2,v1);
        else: s.__rE(v1,v2);
    
    def removeVertex(s,v):
        s.V[v-1] = None; s.l -= 1;
        for i in range(len(s.V)):
            if(i+1 != v): s.removeEdge(i+1,v);
        
    def display(s):
        pic = [];
        for i in range(len(s.V)): pic.append([i+1,s.toArray(i+1)]);
        for e in pic: print(e[0],e[1]);
         
V = 5; E = [(1,2),(1,4),(2,3,5),(2,4),(2,5),(3,4),(3,5)];
G = SparseGraph(V,E,"u"); print(G.contains(5,3));
G.removeEdge(2,4);
G.removeVertex(3);
G.putEdge(3,2)
G.display()
        