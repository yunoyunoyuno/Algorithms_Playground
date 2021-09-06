import time
def T1():
   n = 25000
   list1 = [];t0 = time.time()
   for k in range(n): list1 += [0];
   print(time.time()-t0);
   tuple1 = tuple(); t0 = time.time()
   for k in range(n):tuple1 += (0,);
   print(time.time()-t0);

def N1():
   x = int(input(">> "));
   print(tuple(i for i in range(2,x,2)));

def N2():
   #x = [int(e) for e in list(input())];
   #print(tuple(x));
   #Hardcore!
   x = int(input()); t = tuple();
   while(x > 0):
      d = x%10;
      t = (d,) + t;
      x //= 10;
   print(t)

#-
def N3():
   #Hard mode is when U not using list.count();
   s = list(input()); d = dict();
   for e in s:
      if e not in d: d[e] = 1;
      else: d[e] += 1;
   print(d);


def N4():
   x = set(input()); y = set(input());
   same = x & y;
   print(same);

#!! การใช้ dict ควรเก็บ key พวกประเภท/ ชนิด [ควรดูว่าต้องการอะไร ถ้าถามนิสิตจากคณะ เก็บ key เป็นคณะ]
#!! การ add ลงในset ควรนึกถึง union แทนการเชคว่ามีหรือยังไม่มี (อย่าลืมรับค่าจาก union)
#!! หมั่นเชคบ่อยๆว่า key มีใน dict มั้ย
#PS อย่าลืม sorted
def N5():
   n = int(input()); d = dict();
   for i in range(n):
      name,f = input().strip().split();
      if(f not in d): d[f] = set((name,))
      else: d[f].add(name);
   fs = input().split()
   s = set()
   for f in fs:
      if f in d: s = s.union(d[f]);
   print(" ".join(sorted(s)))
   


def N6():
   n = int(input());
   u = set(); i = set()
   for k in range(n):
      s = set(input().split())
      if(len(i) == 0): i = s;
      else: i = i & s;
      u = u.union(s);
   print(len(u));print(len(i));
      
#ข้ามไป += 1
#ข้ามไป += 1











