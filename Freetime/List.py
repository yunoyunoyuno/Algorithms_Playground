
#1
def N1():
   v1 = [float(e) for e in input("v1: ").split()];
   v2 = [float(e2) for e2 in input("v2: ").split()];
   if(len(v1) != len(v2)): print("2 vectors are not equal sizes"); return;
   k = 0;
   for i in range(len(v1)):
      k += v1[i]*v2[i];
   print(k);
#N1();

#2
def N2():
   n = int(input("n : ")); l = [];
   for _ in range(n):
      k = float(input(" >> ")); l.append(k);
   l.sort(); l = [str(e) for e in l];
   print(",".join(l));
   
#N2();

def N3():
   '''
   fname = input("filename : "); a = [];
   f = open(fname,'r'); ca = [];
   for line in f: a.append(int(line));
   l = min(a); r = max(a);
   for i in range(l,r+1):
      c = a.count(i);
      if(c > 1): ca.append((c,i));
   ca.sort();ca.reverse(); a = [e[1] for e in ca];
   print(a);
   '''

   fname = input("file name : ");
   f = open(fname,"r"); d = []; c = [];
   for e in f: d.append(float(e));
   for n in d: c.append(d.count(n));
   maxc = max(c); out = [];
   for k in range(len(d)):
      if(not d[k] in out and c[k] == maxc): out.append(d[k]);
   for e in out: print(e);

#N3();

def N4():
   fname = input("file_name: ");
   f = open(fname,"r"); t = [];
   for line in f:
      if("<headline>" in line and "</headline>" in line):
         L = line.find("<headline>")+len('<headline>');
         R = line.find("</headline>",L);
         t.append(line[L:R]); 
   f.close();
   t.sort();
   for s in t: print(s);
      

#N4();


def N5():
   f_name = input("file_name: ");
   '''
   #My Method
   f = open(f_name,"r"); t = []; c= [];
   for line in f:
      t.append(line); c.append(len(line.strip()));
   f.close();
   
   c.sort(); ans = [];
   for nt in c:
      for txt in t:
         if(len(txt) == nt and txt not in ans): ans.append(txt);
   ans.sort();
   for e in ans: print(e);
   '''
   #Professor Method.
   d = [];
   f = open(f_name,"r");
   for line in f: d.append(line.strip());
   for i in range(len(d)-1):
      for k in range(len(d)-1):
         if(len(d[k]) > len(d[k+1]) or \
            (len(d[k]) == len(d[k+1]) and \
             d[k] > d[k+1])): d[k],d[k+1] = d[k+1],d[k];
         
   for e in d: print(e);
#N5();
   
#Josephus

def N6():
   n = int(input("n >> "));
   for i in range(1,2*n): 
      q = ['G']*n + ['B']*n;
      m = 2*n;k = 0;
      while(len(q) > 1):
         k = (k+i)%len(q);
         q.pop(k);
      if(q[0] == 'G'): print(i); break;
   else: print("Not Found");   
   

def J():
   m = int(input("m ")); d = int(input("d "));
   q = list(range(m)); k =0;
   while(len(q) > 1):
      k = (k + d)%(len(q));
      q.pop(k);
   print(q[0]);

#N6();


     













   
   
