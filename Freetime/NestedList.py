def N1():
   r,c = [int(e) for e in input("r c ").split()];
   M = [];
   for i in range(r):
      ri = [float (e) for e in input().split()]
      if(len(ri) != c): print([[]]); break;
      M.append(ri);
   else: print(M);

#N1();


def N2():
   fname = input("file_name : ");
   f = open(fname,'r'); M = [];
   for line in f:
      p = line.split();
      M.append([p[0],p[1::]]);
   f.close();
   #print(M);
   return M;
#N2();

def N3():
   M = N2();users = [];uf_u = [];
   for e in M: users.append(e[0]);
   for u in users:
      for e in M:
         if(u in e[1]): break;
      else: uf_u.append(u);
   print(uf_u);
#N3();

def N4():
   '''
   #My Method (Bubble sort way)
   n = int(input(">> ")); s = [];
   for _ in range(n): s.append(input("w : "));
   for i in range(len(s)-1):
      for j in range(i+1,len(s)):
         if(len(s[j]) < len(s[i])): s[j],s[i] = s[i],s[j];
         elif(len(s[j]) == len(s[i]) and s[j] < s[i]):
            s[j],s[i] = s[i],s[j];
   print(s);
   '''
   # Professor Method.
   n = int(input(">> ")); s = [];
   for _ in range(n):
      w = input("").strip()
      s.append([len(w),w]);
   s.sort();
   for [l,a] in s: print(a);

#N4();

#!!!
def N5():
   n,m = [int(e) for e in input(">> ").split()];
   invalid_user = []; data = [];
   for _ in range(n):
      t = input(" ").split();
      if(len(t) == m+1): data.append([-sum([float(k) for k in t[1::]]),t[0]]);
      else: invalid_user.append(t[0]);
   if(len(invalid_user)!=0):
      print("Invalid data:");[print(e) for e in invalid_user];
   else:
      data.sort();
      [print(e[1],-1*e[0]) for e in data];

N5();

























