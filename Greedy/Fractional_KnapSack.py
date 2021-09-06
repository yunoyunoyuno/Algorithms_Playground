def merge(A,L,M,R):
    p1 = L;p2 = M+1; U = [None for _ in range(L,R+1)]
    for k in range(len(U)):
        if(p1 >= M+1): U[k] = A[p2]; p2+= 1; continue;
        elif(p2 > R): U[k] = A[p1]; p1 += 1; continue;
        elif(A[p1].cost() >= A[p2].cost()): U[k] = A[p1]; p1 += 1;
        elif(A[p2].cost() > A[p1].cost()): U[k] = A[p2]; p2 += 1;
    for i in range(L,R+1): A[i] = U[i-L];

def msR(A,L,R):
    if(L < R):
        mid = (L+R)//2;
        msR(A,L,mid);
        msR(A,mid+1,R);
        merge(A,L,mid,R);

def mergeSort(A):
    msR(A,0,len(A)-1);

class Node:
    x = 0;
    def __init__(self,v,w):
        self.val = v;
        self.weight = w;
        
    def cost(self):
        return self.val/self.weight;

Test = [(22,60),(32,70),(30,80)]
Items = [];

for e in Test: Items.append(Node(e[0],e[1]));

def ans(A,w):
    total = 0;
    print("There is 1 bag can contains only",w,"kg");
    for i,e in enumerate(A):
        print("Items",i+1,"cost",e.val,"weight",e.weight,"kg");
    print("To put as much value as you can");
    for i in range(len(A)):
        if(A[i].x > 0):
            print("Put item",i+1,"with portion",Items[i].x,"in the bag");
            total += A[i].val*A[i].x
    print("Total values : ",total);
    
#Fractional Knapsack;
mergeSort(Items);

weight = 100; totalW = 0;
for k in range(len(Items)):
    iw = Items[k].weight;
    if(totalW + iw <= weight):
        Items[k].x = 1;
    else:
        Items[k].x = (weight-totalW)/iw
    totalW += iw* Items[k].x;

ans(Items,weight);















    
