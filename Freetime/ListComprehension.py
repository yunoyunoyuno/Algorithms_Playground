def N1():
   c = 'a';x = ['abba','babana','ann'];
   d = [s.count(c) for s in x];
   print(d);

def N2():
   x = [1,2,-1,-5,-9,100];
   pl = [e for e in x if e >= 0];
   print(pl);

def N4():
   print(sum([1 for c in input().split() if int(c) < 0 ]));

def N5():
   print("".join([e for e in input() if 'a' <= e.lower() <= 'z']))

def N6():
   x = [int(e) for e in input("1 ").split()];
   y = [int(e) for e in input("2 ").split()];
   z = [x[i] + y[i] for i in range(len(x))];
   print(z);

def N7():
   m = [[1,2,3],[4,5,6]]
   k = [e for row in m for e in row];
   print(k);
#*
def N8():
   x = [int(e) for e in input().split()];
   x.sort();
   y = [x[i] for i in range(len(x)-1) if x[i] != x[i+1]] + [x[-1]];
   print(y);

#***
def N9():
   N = int(input());
   x1 = [j for i in range(2,N//2) for j in range(2*i,N,i)];
   x1.sort();
   c1 = [x1[i] for i in range(len(x1)-1) if x1[i]!=x1[i+1]] + [x1[-1]];
   print(c1);
#**
def N10():
   N = int(input());
   x = [j for i in range(2,N//2) for j in range(2*i,N,i)];
   x.sort();
   x = [x[i] for i in range(len(x)-1) if x[i] != x[i+1]] + [x[-1]];
   y = [k for k in range(2,N) if k not in x];
   print(y); #all prime numbers < N

#Nice Trick
def N11():
   n,m = [int(e) for e in input().split()]
   d = [input().strip().split() for _ in range(n)];
   err = [e[0] for e in d if len(e) != m+1]
   if(len(err) > 0):
      print("Invalid Input");
      print("\n".join(err));
   else:
      d = [[-sum([float(e) for e in x[1:]]),x[0]] for x in d]
      d.sort();
      for [score,user] in d: print(user,-score);

def N12():
   d = [];
   while(True):
      n = int(input());
      d.append(n);
      if(n < 0): break;
   k = [d[-1] + d[i] for i in range(len(d)-1)];
   for a in k: print(a);

def N13():
   d = [];
   while(True):
      k = int(input())
      if(k < 0): break;
      d.append(k);
   c = [k for k in d if d.count(k) > len(d)//2];
   if(len(c) == 0): print("Not Found"); return;
   c.sort(); c = [c[i] for i in range(len(c)-1) if c[i] != c[i+1]] + [c[-1]];
   for e in c: print(e);







































   
   
