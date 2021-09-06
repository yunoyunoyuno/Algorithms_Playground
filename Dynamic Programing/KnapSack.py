# 0/1 KnapSack Problem
#Items = [(20,2),(30,2),(66,3),(40,4),(60,5)];
v = [10,30,40,5,12];w = [25,34,41,22,60];
Items = [(v[i],w[i]) for i in range(len(v))];
def getV(Items,W):
    n = len(Items);M = [[0 for _ in range(W+1)] for _ in range(n)];
    p= V(Items,n-1,W,M); print("There is ",W,"kg. bag");
    for i,e in enumerate(Items): print("Items",i+1,"weight",e[1],"kg. price",e[0])
    print("The most hightest value in the",W,"kg. bag is",p);
    
def V(Items,i,j,M):
    wi = Items[i][1]; vi = Items[i][0];
    if(i < 0 or j < 0): return 0;
    elif(M[i][j] > 0): return M[i][j];
    elif(j - wi >= 0): M[i][j] =  max(V(Items,i-1,j,M),V(Items,i-1,j-wi,M) + vi)
    else: M[i][j] =  V(Items,i-1,j,M);
    return M[i][j]

def V_btmUp(Items,W):
    n = len(Items); M = [[0 for _ in range(W+1)] for _ in range(n+1)];
    for i in range(n+1): M[i][0] = 0; M[0][i] = 0;
    for i in range(1,n+1):
        cur_weight = Items[i-1][1]; cur_val = Items[i-1][0];
        for j in range(1,W+1):
            if(j - cur_weight < 0): M[i][j] = M[i-1][j];
            else: M[i][j] = max(cur_val + M[i-1][j-cur_weight],M[i-1][j]);
    return M;

def VF(Items,W):
    n = len(Items);
    M = [[0 for _ in range(W+1)] for _ in range(n+1)];
    D = [[0 for _ in range(W+1)] for _ in range(n+1)];
    for i in range(n+1): M[i][0] = 0; M[0][i] = 0;
    for i in range(1,n+1):
        wi = Items[i-1][1]; vi = Items[i-1][0];
        for j in range(1,W+1):
            if(j-wi < 0):
                M[i][j] = M[i-1][j];D[i][j] = 'F'
            else:
                if(M[i-1][j] > vi + M[i-1][j-wi]):
                     M[i][j] = M[i-1][j]; D[i][j] = "F";
                else:
                    M[i][j] = vi + M[i-1][j-wi]; D[i][j] = "T"
    return M,D;

def findKnapSackFat(Items,W):
    v,D = VF(Items,W); s = []; i = len(D)-1;j = W;n = len(Items);
    while(i > 0 and j > 0):
        if(D[i][j] == "F"): i -= 1;
        else: wi = Items[i-1][1]; s.append(i); j -= wi; i-= 1;
    for i,e in enumerate(Items): print("Items",i+1,"weight",e[1],"kg. price",e[0])
    print("There is ",W,"kg. bag");
    for i in s:
        wi = Items[i-1][1]; vi = Items[i-1][0]
        print("Put item",i,"with",wi,"kg. price",vi,"in that bag.")
    print("So the highest value in the bag must be",v[n][W]);
    return s;

def findKnapSackSlim(Items,W):
    M = V_btmUp(Items,W); s = [];i=n=len(Items); j = W;
    while(i > 0 or j > 0):
        wi = Items[i-1][1]; vi = Items[i-1][0];
        if(j - wi >= 0 and vi + M[i-1][j-wi] > M[i-1][j]):
            s.append(i); i-= 1; j -= wi;
        else : i -= 1;  
    for i,e in enumerate(Items): print("Items",i+1,"weight",e[1],"kg. price",e[0])
    print("There is ",W,"kg. bag");
    for i in s:
        wi = Items[i-1][1]; vi = Items[i-1][0]
        print("Put item",i,"with",wi,"kg. price",vi,"in that bag.")
    print("So the highest value in the bag must be",M[n][W]);
    return s;
    
ans = findKnapSackSlim(Items,100);
