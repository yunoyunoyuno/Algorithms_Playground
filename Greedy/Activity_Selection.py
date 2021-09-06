class AC:
    def __init__(self,s,f):
        self.s = s; self.f = f;
                
def sortA(A):
    sortAR(A,0,len(A)-1);

def ans(S,A):
    a = [];
    for e in A: a.append((e.s,e.f));
    print("Activities"); print(a);
    l = list(S);
    s = "";
    for i in l: s += "activity "+str(i+1) + " "
    print(s);
    return s;

def ats(A):
    sortA(A); s = set(); s.add(0);j = 0;
    for i in range(1,len(A)):
        if(A[i].s >= A[j].f):
            s.add(i); j = i
    return ans(s,A)

def sortM(A):
    sortMR(A,0,len(A)-1);

def merge(A,s,m,f):
    U = [None for i in range(s,f+1)];
    p1 = s; p2 = m+1
    for k in range(len(U)):
        if(p1 == m+1): U[k] = A[p2]; p2-=1; continue;
        elif(p2 == f+1): U[k] = A[p1]; p1 += 1; continue;
        elif(A[p1].f <= A[p2].f): U[k] = A[p1]; p1+=1; 
        elif(A[p2].f < A[p1].f): U[k] = A[p2]; p2 += 1;
    for i in range(s,f+1): A[i] = U[i-s];
    

def sortAR(A,s,f):
    mid = (s+f)//2;
    if(s < f):
        sortAR(A,s,mid);
        sortAR(A,mid+1,f);
        merge(A,s,mid,f);

act = [(0.48,16.46),(11,14),(14,20),(12.51,13.52),(14.25,16.38),(8.07,18.33)];
a = []
for c in act:
    e = AC(c[0],c[1])
    a.append(e)

s = ats(a);



    
