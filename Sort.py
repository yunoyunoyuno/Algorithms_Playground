import matplotlib.pyplot as plt
import random;

Y = [];X=[];y0 = [];correct = []
x = [];N = 500
for i in range(N):
    y0.append(N);x.append((N-i)/N);
    correct.append(i);


def merge(A,L,M,R):
    p1 = L; p2 = M+1;y = []
    U = [None for i in range(L,R+1)];
    for k in range(len(U)):
        if(p1 == M+1 ): U[k] = A[p2]; p2 += 1;
        elif(p2 > R): U[k] = A[p1]; p1 += 1;
        elif(A[p1] < A[p2]): U[k] = A[p1]; p1 += 1;
        elif(A[p2] <= A[p1]): U[k] = A[p2]; p2 += 1;
    for i in range(L,R+1): A[i] = U[i-L];
    
    for i in range(len(Y[0])):
        k = Y[-1][:];
        y.append(k[i]-1)
    Y.append(y);
    test = A[:]
    X.append(test);
        
        

def msr(A,L,R):
    if(L < R):
        M = (L+R)//2;
        msr(A,L,M);
        msr(A,M+1,R);
        merge(A,L,M,R);

def mergesort(A):
    msr(A,0,len(A)-1);


def selection_sort(A):
    for i in range(len(A)):
        mI = i; y = [];
        for j in range(i+1,len(A)):
            if(A[j] < A[mI]): mI = j;
        A[i],A[mI] = A[mI],A[i];
        t = A[:];
        X.append(t);
        for i in range(len(Y[0])):
            k = Y[-1][:];
            y.append(k[i]-1)
        Y.append(y);

def partition(A,L,R):
    p = A[L];i = L + 1; j = R-1; y= [];
    while(i < j):
        while(i < R and A[i] < p ): i += 1;
        while(A[j] > p):  j -= 1;
        if(i < j): A[i],A[j] = A[j],A[i];
    if(A[j] < p): A[L],A[j] = A[j],A[L];
    for c in range(len(Y[0])):
        k = Y[-1][:];
        y.append(k[c]-1)
    Y.append(y);
    test = A[:]
    X.append(test);
    return j;

def qR(A,L,R):
    if(L < R):
        j = partition(A,L,R);
        qR(A,L,j);
        qR(A,j+1,R);

def quickSort(A):
    qR(A,0,len(A));

def shell_sort(l = []): # Sedgewick
    h = len(l)//2
    while(h > 0):
        for m in range(h):
            for i in range(m + h,len(l),h): #insertion sort.
                t = l[i]; j = i-h;
                while(j >= 0 and t < l[j]):
                    l[j+h] = l[j]; j -= h;
                    tmp = l[:]; X.append(tmp);y =[];
                    for c in range(len(Y[0])):
                        k = Y[-1][:];
                        y.append(k[c]-1)
                    Y.append(y);
                l[j+h] = t;
        h //= 2;

def percolate_down(l,i,size): # Max Heap.
    c = 2*i+1;y = []
    while( c < size): # while remain left child
        if(c+1 < size and l[c+1] > l[c]): c+= 1 #consider right child.
        if(l[i] >= l[c]): break;
        l[i],l[c] = l[c],l[i];
        i = c;c = 2*i+1
    t = l[:];
    X.append(t);
    for i in range(len(Y[0])):
        k = Y[-1][:];
        y.append(k[i]-1)
    Y.append(y)

def heap_sort(l = []):
    for i in range(len(l)//2-1,-1,-1):
        percolate_down(l,i,len(l)); # build a heap.
    for j in range(len(l)-1,-1,-1):
        l[0],l[j] = l[j],l[0];
        percolate_down(l,0,j);

def bubble_sort(l):
    is_sorted = True;
    for i in range(len(l)):
        for j in range(1,len(l)):
            y = [];
            if(l[j] < l[j-1]):
                l[j-1],l[j] = l[j],l[j-1];
                t = l[:];
                X.append(t);
                for i in range(len(Y[0])):
                    k = Y[-1][:];
                    y.append(k[i]-1)
                Y.append(y)
            is_sorted = False
        if(is_sorted): break;

random.shuffle(x);
Y.append(y0);
#mergesort(x);
X.append(x[:]);
quickSort(x);
random.shuffle(x);
selection_sort(x);
random.shuffle(x);
mergesort(x);title = "Merge Sort";cmap = 'rainbow'
#selection_sort(x); title = "Selection Sort"; cmap = 'jet'
#quickSort(x); title = "Quick Sort"; cmap = "CMRmap";
#shell_sort(x); title = "Shell Sort (SedgeWick)"; cmap = "gnuplot2"
heap_sort(x); title = "( Quick + Selection + Merge + Heap )*Sort"; cmap = "turbo";
#bubble_sort(x); title = "Bubble Sort"; cmap = "magma"; #N=140

Hfont = {'fontname':'Candara'};
Xfont = {'fontname':'monospace'};
plt.figure(dpi=300)
for i in range(len(X)):
    plt.scatter(correct,Y[i],s=0.06, c=X[i], cmap=cmap,marker = "s")
    
  
cbar = plt.colorbar(shrink = 0.75,pad = 0.03)
cbar.ax.tick_params(labelsize=4) 


plt.title("Made By YN",**Xfont,size=4,loc = "right");
plt.title(title,fontsize=8,**Hfont,pad = 5)
plt.tick_params(axis='x', labelsize=4)
plt.tick_params(axis='y', labelsize=4)
plt.show()




