import numpy as np;

class Stack:
    s ,data = 0, np.zeros(1,dtype="object");
    def size(self): return self.s;
    def is_empty(self): return self.s == 0;
    def peek(self): return self.data[self.s-1];
    def push(self,obj):
        if(self.s >= len(self.data)):
            d = np.zeros(len(self.data)*2,dtype="object");
            for i in range(self.s): d[i] = self.data[i];
            self.data = d;
        self.data[self.s] = obj; self.s += 1;
    def pop(self):
        e = self.data[self.s-1]; 
        self.data[self.s-1] = 0.0;self.s -= 1;
        return e;

def valid_parentheses(p):
    op,cl = "[{(","]})";
    stack = Stack();
    for s in p:
        if(s in op): stack.push(s);
        elif(s in cl):
            k = cl.index(s);
            o = stack.pop();
            if(op.index(o) != k): return False;
        elif(stack.is_empty()): return False;
    else: return stack.is_empty();
        
t = "{x=b[5*(x+c[i+2])+8]+(3*d)}";
f1 = "(b[2+5]"
f2 = "b[2+5]"
f3 = "b[2+5}"
f_cases = [f1,f2,f3];
for f in f_cases: print(valid_parentheses(f));
print(valid_parentheses(t));



class List:
    s= 0;

    @staticmethod
    def to_List(d):
        L = List(len(d));
        for e in d: L.append(e);
        return L;

    def __init__(self,m=1):
        self.data = np.zeros(m,dtype="object");

    def __assert_in_range(self,i,m):
        assert(not(i < 0 or i > m)),"i out of bounds !";

    def __index_of(obj):
        for i in range(self.s):
            if(self.data[i] == obj): return i;
        return -1;

    def size(self): return self.s

    def add(self,i,obj):
        self.__assert_in_range(i,self.s);
        if(self.s >= len(self.data)):
            d = np.zeros(len(self.data)*2,dtype="object");
            for k in range(self.s): d[k] = self.data[k];
            self.data = d;
        for j in range(i,self.s-1): self.data[j+1] = self.data[j];
        self.data[i] = obj;
        self.s += 1;

    def append(self,obj):
        self.add(self.s,obj);

    def pop(self,i=-1):
        if(i == -1): i = self.s-1;
        self.__assert_in_range(i,self.s-1);
        for k in range(i,self.s-1): self.data[k] = self.data[k+1];
        self.data[self.s-1] = 0.0
        self.s -= 1;

    def remove(self,obj):
        k = self.__index_of(obj);
        if(k == -1): return;
        self.pop(k);

    def get(self,i):
        self.__assert_in_range(i,self.s-1);
        return self.data[i];

    def set(self,i,obj):
        self.__assert_in_range(i,self.s-1);
        self.data[i] = obj;

    def contains(self,obj): return self.node_of(obj) != -1;

    def to_list(self): return [e for e in self.data if e != 0];

    

def infix2postfix(infix : List):
    operators = "+-*/^"
    cost = List.to_List(np.array([3,3,5,7],dtype=int));
    s = Stack();
    postfix = List();
    for i in range(infix.size()):
        e = infix.get(i);
        if(e not in operators): postfix.append(e); continue;
        elif(not s.is_empty()):
            o = s.peek(); oc = cost.get(operators.index(o));
            ec = cost.get(operators.index(e));
            while(s.size() > 0 and oc > ec): postfix.append(s.pop());
        s.push(e);
    while(not s.is_empty()): postfix.append(s.pop());
    return postfix;

prefix = List.to_List("a+b*c");
r = infix2postfix(prefix);
print(r.to_list());
        


























