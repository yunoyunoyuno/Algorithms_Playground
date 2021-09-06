import matplotlib.pyplot as plt;
import random;
import math;
from matplotlib import animation,rc;
import pandas as pd;

# dist(a,b) => shortest distance from a => b
# When swap any 2 nodes the edges have little change (4 edges).(dE)

def next_path(k,X,Y,tour_log,line,txt):
   T,tour = tour_log[k];
   N = len(tour);
   d = sum([M[tour[i]][tour[i-1]] for i in range(N)]);
   txt.set_text(f"T = {round(T,7)} tour length = {round(d,3)}");
   x = [X[p] for p in tour] + [X[tour[0]]];
   y = [Y[p] for p in tour] + [Y[tour[0]]];
   line.set_data(x,y);
   if(k == len(tour_log)-1):
      line.set_color('red');
      txt.set_color('red');
   return (line,txt);
   

def animate(X,Y,tour_log = []):
        fig,ax = plt.subplots();
        line, = ax.plot(X,Y,color = 'blue');
        line.set_marker('o');
        line.set_markersize(6);
        minX,maxX = min(X),max(X);
        minY,maxY = min(Y),max(Y);
        w = maxX-minX; h = maxY-minY;
        width = 6 if w > h else 6 * w/h; 
        height = 6 if h > w else 6 * h/w;
        fig.set_size_inches(max(4,width),max(4,height)); #each gap size (min 4);
        dy = abs(0.1 * (maxY-minY)); #10% of Y;
        txt = ax.text(minX,minY-1.7*dy,"SA",fontsize = 10);
        ax.set_ylim(minY - 2*dy,maxY+dy);
        ani = animation.FuncAnimation(fig,next_path,
                                          frames = len(tour_log),
                                          fargs = [X,Y,tour_log,line,txt],
                                          interval = 10,repeat = False,
                                          blit = True);
        plt.show()

def read_map(map_name):
        X = []; Y = [];
        f = open(map_name);
        for line in f:
                if line.strip() == 'EOF': break;
                d = line.split();
                X.append(float(d[1])); Y.append(float(d[2]));
        f.close();
        return (X,Y);

def d(x,y): return (x**2 + y**2)**0.5
def dist(i,j): return M[i][j];

def calc_all_pair_distances(X,Y):
   n = len(X);
   D = [[0.0]*n for _ in range(n) ];
   for i in range(n):
      for j in range(i+1,n):D[i][j] = D[j][i] = d(X[i]-X[j],Y[i]-Y[j]);
   return D;

X,Y = [],[];
map_name = input("map file name (eg. simple.txt) : ");
if(map_name != "TH"): X,Y = read_map(map_name); # co-ordinates must be number;
else:
   df = pd.read_csv("th.csv");
   cap = df[(df.capital == 'primary') | (df.capital == 'admin')];
   latlng = cap[["lat","lng"]].values.tolist();
   X = [e[0] for e in latlng];Y = [e[1] for e in latlng];

N = len(X); t = list(range(N));
T = N*10 # From Profressor.
K = 1.38064852; tour_log = []
M = calc_all_pair_distances(X,Y);

while(T > 0.0000001):
   i = random.randint(0,N-2); j = random.randint(i,N-1);
   s = list(t);
   s[i],s[j] = s[j],s[i];
   #Re calculate distance.
   dE = dist(s[i],s[i+1]) + dist(s[i-1],s[i])      + \
        dist(s[j-1],s[j]) + dist(s[j],s[(j+1)%N])  + \
        - dist(t[i-1],t[i]) - dist(t[i],t[i+1])    + \
        - dist(t[j-1],t[j]) - dist(t[j],t[(j+1)%N]);
   if(dE < 0 or random.random() < math.e ** -(dE)/K*T): t = s;
   T *= 0.995
   tour_log += [[T,t]];
animate(X,Y,tour_log)

   
                   

#Final animate(X,Y,tour_log)❌


'''
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

'''




# Go to supermarket.





















    
















    
