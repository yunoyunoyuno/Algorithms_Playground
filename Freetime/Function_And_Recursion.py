
#3
def g(m,b,n,c):
   if(m==n and b==c): return 2;
   elif(m==n and b != c): return 1;
   return ((b-c)/(n-m),m*(b-c)/(n-m) + b);

#4
def h(x):
   return [e for e in x if e%2 == 0]

#5
def a(n):
   if(n == 0): return 1;
   if(n == 1): return 2;
   return a(n-2)*n;

#6
def k(n):
   if(n == 0): return 1;
   if(n == 1): return 2;
   if(n%2 == 1): n = (n-1)/2; return k(n-1)*n;
   x = k(n/2); return x + x%10
   
def N7():
   i,j,k = [int(e) for e in input().split()]
   def s(i,k):
      if(i >= k): return 0;
      return k + t(i+1,k);
   def t(j,k):
      if(j >= k): return 0;
      return j + s(j,k-1);
   print(s(i,k)); print(t(j,k));


#***
def is_pR(s,l,r):
   if(l >= r): return True;
   if(s[l] == s[r]):
     return  is_pR(s,l+1,r-1);
   else: return False;

def is_palindrome(s):
   return is_pR(s,0,len(s)-1);

def is_palinD(s):
 if(len(s) <= 1): return True;
 if(s[0] != s[-1]): return False;
 return is_palinD(s[1:-1])


#DAYS BETWEEN YEARS **** (Nice Design)
def N8():
   def is_leap_year(y):
      return y%4 == 0 and (y%100==0 or y%400==0);

   def days_of_year(d,m,y):
      D = [31,28,31,30,31,30,31,31,30,31,30,31];
      if(is_leap_year(y)): D[1] += 1;
      for i in range(m-1): d += D[i];
      return d

   def days_in_years(y):
      return 366 if is_leap_year(y) else 365;
   
   d1,m1,y1 = [int(e) for e in input().strip().split()];
   d2,m2,y2 = [int(e) for e in input().strip().split()];
   
   d_a = days_of_year(d1,m1,y1);
   d_b = days_of_year(d2,m2,y2);

   c = 0;
   for y in range(y1+1,y2): c += days_in_years(y)
   
   print(days_in_years(y1) - d_a + 1 + c + d_b)




#Recursive sum list ***
# เรียกซ้ำและวงวนเป็นเพื่อนกัน
def sumlist(x):
   if(len(x) == 0): return 0;
   if(len(x) != 0):
      c = 0;
      for l in x:
         if(type(l) == list): c += sumlist(l);
         else: c += l;
      return c;



