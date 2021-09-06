import random;

class maxHeap:
    data = []; l = 0;
    def __gt(s,i,j):
        return s.data[i][1] > s.data[j][1];
    def __fU(s,j):
        while(j > 0):
            p = (j-1)//2;
            if(s.__gt(j,p)): s.data[p],s.data[j] = s.data[j],s.data[p];
            j = p;
    def __fD(s,p):
        while(2*p + 1 < s.l):
            c = 2*p + 1 ;
            if(c+1 < s.l and s.__gt(c+1,c)): c+=1;
            if(s.__gt(c,p)): s.data[c],s.data[p] = s.data[p],s.data[c];
            p = c;
    def deQ(s):
        e = s.data[0];
        s.data[s.l-1],s.data[0] = s.data[0],s.data[s.l-1];
        s.data.pop(); s.l -= 1; s.__fD(0);return e;
    def enQ(s,obj):
        s.data.append(obj);s.__fU(s.l);s.l += 1;
    def size(s): return s.l;
    def toA(s): return s.data

def partition(A,L,R):
    p = A[L].cost; i = L +1; j = R;
    while(i < j):
        while(i < R and A[i].cost >= p): i+=1; 
        while(A[j].cost < p): j -= 1;
        if(i < j): A[i],A[j] = A[j],A[i];
    if(p < A[j].cost): A[L],A[j] = A[j],A[L];
    return j;

def qR(A,L,R):
    if(L < R):
        j = partition(A,L,R);qR(A,L,j-1); qR(A,j+1,R);
def quickSort(A): qR(A,0,len(A)-1);
class Item:
    def __init__(s,v,w): s.v = v; s.w = w; s.cost = v/w;
    
def SV(X,I): return sum([X[i]*I[i].v for i in range(len(X))]);
def SW(X,I): return sum([X[i]*I[i].w for i in range(len(X))]);
def FKS(I,W,L):
    ANS = [];tW = 0;
    for i in range(L,len(I)):
        if(W - I[i].w >= 0): ANS.append(1); W -= I[i].w
        else:  ANS.append((W - I[i].w)/I[i].w); break;
    return SV(ANS,I);

#A = FKS(Items,100); k = S(A,Items,3);
#H = maxHeap();


def KnapSack(Items,W):
    quickSort(Items); Vmax = -1;Xmax = [];
    H = maxHeap();H.enQ(([],FKS(Items,W,0)));
    while(H.size() > 0):
        (X,Vub) = H.deQ(); m = len(X)-1;
        if(Vub <= Vmax): break;
        if(len(X) == len(Items) and Vub > Vmax):Vmax = Vub; Xmax = X;
        else:
            sv = SV(X,Items); sw = SW(X,Items);
            X0 = X[:]; X0.append(0);
            H.enQ((X0,sv + FKS(Items,W-sw,m+2)));
            if(W-sw-I[m+1].w >= 0):
                X1 = X[:]; X1.append(1);m = len(X)-1;
                H.enQ((X1,sv + Items[m+1].v + FKS(Items,W-sw-Items[m+1].w,m+2)));
    return (Vmax,Xmax);

I = [(random.randint(1,90),random.randint(1,90)) for i in range(600)];
I = [Item(e[0],e[1]) for e in I];

def ANS(I,W):
    V,X = KnapSack(I,W);
    print("There is",W,"kg. bag");
    print("There are",len(I),"Items");
    [print((i+1,"val",I[i].v,"weight",I[i].w)) for i in range(len(I))];
    w = 0;
    for i in range(len(X)):
        if(X[i] > 0): print("Put",i+1,"in bag");w += I[i].w
    print("You will get maximum cost",V,"Weight",w);


ANS(I,100);












            


'''
E = [(4,10),(6,2),(1,8),(3,2),(10,100)];
for e in E: H.enQ(e);
for e in E: print(H.deQ());

'''












