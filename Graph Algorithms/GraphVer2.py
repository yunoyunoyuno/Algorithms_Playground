class Q:
    data = [None]; size = 0; front = 0;
    def length(s):return s.size;
    def enqueue(s,obj):
        if(s.size == len(s.data)):
            m = [None] * 2*len(s.data); i = 0;j = s.front;
            for i in range(s.size):
                m[i] = s.data[j]; j = s.__inc(j);
            s.front = 0; s.data = m;
        j = (s.front + s.size)%len(s.data); s.data[j] = obj; s.size += 1;
        
    def dequeue(s):
        e = s.data[s.front];s.data[s.front] = None;
        s.front = s.__inc(s.front); s.size -= 1;
        return e;
            
    def __inc(s,i): return (i+1)%len(s.data);

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
    
def shortestPath(G,s,t):
    n = G.size(); p = [None for _ in range(n)]; d = [1e5 for _ in range(n)]; q = Q(); q.enqueue(s);d[s-1] = 0;
    while(q.length() > 0):
        u = q.dequeue();
        for v in G.adj(u):
            k = v[0] - 1;
            if(d[k] == 1e5): d[k] = d[u-1] + 1;p[k] = u; q.enqueue(v[0]);
    k = n-1; path = str(n);
    while(k > s):
        path = str(p[k]) + "->" +path; k -= 1;
        if(p[k] == s): break
    path = str(s) +"->"+path;
    print("Moving from",path,"with distance",d[-1]);
    
        
V = 6; E = [(1,2),(1,3),(2,4),(3,4),(4,5),(5,6)]
G = Graph(V,E,"u");        
G.display()
shortestPath(G,3,6);
'''
print(G.contains(5,3));
G.removeEdge(2,4);
G.removeVertex(3);
G.addEdge(3,2)
G.display();

a = [];b = Q();
'''












'''
Big = [i for i in range(10**6)]
for i in Big: a.append(i); b.enqueue(i);
print("Let do racing ...");
for i in Big:
    b.dequeue();
print("Queue is Finished");
for i in Big:
    a.pop(0);
print("Array Queue is Finished");
'''
'''        
A = [1,2,3,4,5];q = Q();
for a in A: q.enqueue(a);
q.dequeue(),q.dequeue();
A = [6,7,8,9,10]
for a in A: q.enqueue(a);
while(q.length() > 0):
    print(q.dequeue())
'''
            