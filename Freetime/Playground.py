def selectionSort(A):
   #A[0..n-1]
   for i in range(len(A)-1,0,-1):
      mi = 0; # n-1
      for j in range(1,i+1):#∑[2,n]{i}
         if(A[mi] < A[j]): 
            mi = j;#∑[2,n] {(i-1)} <max>
      A[i],A[mi] = A[mi],A[i] # n-1;

A = [5,4,1,2,6];

selectionSort(A); print(A);

#∀f,g{Θ(f(n)+g(n)) = Θ(max(f(n),g(n)))}; 

#if P1 => P2 else P3 (t1,t2,t3)
# => t ∈[t1 + min(t2,t3),t1 + max(t2,t3)]
#for => ∑[1,m]ti ∀i ∈ N ∩ [1,2,...,m]
# Hn ∈ O(logn)
#(∫[m-1,n]{1/k}<= ∑[m,n]{1/k} <= ∫[m,n+1]{1/k})






#วัชรพัฒน์ เมตตานันท






















































