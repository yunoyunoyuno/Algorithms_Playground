import numpy as np;
# Shorter => Faster!

#1* Process can be done in 1 line!
def N1():
   M = np.array([[1,2,3],[4,5,6],[7,8,9]]);
   k = int(input());
   ''' Work but ...
   for i in range(len(M)):
      for j in range(len(M[i])):
         if(i%k == 0 and j%k == 0): M[i,j] = 0;
   print(M);
   '''
   M[::k,::k] = [0];
   print(M);

#** some technique...
def N2():
   M = np.array([[1,2,3],[4,5,6],[7,8,9]]);
   k = int(input());
   '''
   N = np.zeros_like(M);
   N[::k,::k] = 1;
   M += M*N;
   '''
   M[::k,::k] *= 2;print(M);

#* np.max,np.min กำหนด axis มันหาทุกแบบเช่น axis = 0 ก้หามาให้ทุกแนวตั้้ง
def N3():
   M = np.array([[3,2],[5,6],[7,1]]);
   mx = np.max(M,axis = 0); mn = np.min(M,axis = 0);
   print(mx-mn);

#*** เลือกสมาชิกเป็นตัว ๆ (ไม่ใช่เป็น array)
def N4():
   X = np.array([[3,4],[5,12],[24,7]])
   Y = (X[:,0]**2 + X[:,1]**2)**0.5
   print(Y);

#สร้างตาราง เทคนิคใหม่

   
def N5():
   k = int(input());
   C = np.ones([k,k],int);
   C[::2,::2] = C[1::2,1::2] = 0;
   print(C);

#**** จากทรงเหมือนต้องใช้ loop
#ลองดึงค่าคงที่ดูครับ
def N6():
   k = int(input());
   M = np.zeros([k,k],int);
   M[::2,::2]= M[1::2,1::2] =1;
   print((M*(np.arange(1,k+1))).T)
   
#Votes *** Apply numPy
def N7():
   n= int(input().strip());
   S = []
   for _ in range(n):
      S.append([float(s) for s in input().strip().split()]);
   #(n,3) and (1,3) => (n,3)
   W = [float(w) for w in input().strip().split()];
   S = np.array(S); W = np.array(W);
   S *= W; #broad cast.
   R = np.sum(S,axis=1)
   for e in R: print(e);
   
# Rent Prices **
def N8():
   P = np.array([int(e) for e in input().strip().split()]);
   db = [];
   db = np.array([[int(p) for p in input().split()] for _ in range(4)]);
   R = np.sum((db.T*P).T,axis=0);
   DAYS = ["Mon","Tue","Wed","Thu","Fri"];
   max_book_day = np.argmax(np.sum(db,axis=0));
   n_max_book = np.sum(db[:,max_book_day],axis=0);
   print(DAYS[max_book_day],n_max_book);
   print(" ".join([str(r) for r in R]));
   #R = np.sum(db,axis=1); print(R);
'''
50 30 40 20
20 50 10 15 20
30 40 20 65 35
75 30 42 70 45
40 25 35 22 55
'''













































   








