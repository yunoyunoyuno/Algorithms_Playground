import numpy as np;

class List:
    s,data = 0,np.array([None],dtype = "object");
    
    def __assert_in_range(self,i,m):
        if(i < 0 or i > m): assert(True),"＞﹏＜ index out of range"
        
    def __ensure_cap(self):
        if(self.s >= len(self.data)):
            m = np.array([None] * len(self.data)*2,dtype = "object");
            for i in range(self.s): m[i] = self.data[i];
            self.data = m;
            
    def __assert_not_none(self,obj):
        if(obj == None):
            assert(True),"Sry, None is not allow for insert（＞人＜；）";
        
    def is_empty(self): return self.s == 0;
    
    def size(self): return self.s;
    
    def index_of(self,obj):
        for i in range(self.s):
            if(self.data[i] == obj): return i;
        return -1
    def get(self,i):
        self.__assert_in_range(i,self.s-1); return self.data[i];
    
    def contains(self,obj): return self.index_of(obj) != -1;
    
    def append(self,obj):
        self.add(self.s,obj);
        
    def add(self,i,obj):
        self.__ensure_cap();
        self.__assert_not_none(obj);
        self.__assert_in_range(i,self.s);
        for k in range(i,self.s-1): self.data[k+1] = self.data[k];
        self.data[i] = obj; self.s += 1;

    def remove(self,obj):
        self.__assert_not_none(obj);
        i = self.index_of(obj);
        self.pop(i,obj);
        
    def pop(self,i=-1):
        if(i == -1): i = self.s-1
        self.__assert_in_range(i,self.s-1);
        for k in range(i+1,self.s): self.data[k-1] = self.data[k];
        self.data[self.s-1] = None; self.s -= 1;

    def set(self,i,obj):
        self.__assert_in_range(i,self.s-1);
        self.data[i] = obj;
        
   
x = List();
x.add(0,"A");
x.append("B");
x.add(0,"C");
x.set(2,"D");
x.pop(1);
for i in range(x.size()): print(x.get(i));


class SLLWH:
    class LinkedNode:
        def __init__(self,e,n): self.element,self.next = e,n;

    header,s = LinkedNode(None,None),0;

    def __assert_not_none(self,obj):
        assert(not(obj == None)),"None is not accept!";
        
    def __assert_in_range(self,i,m):
        assert(not(i < 0 or i > m)),"Range should ∈ [0,n-1]";

    def __rm_after(self,p):
        if(p.next != None):
            p.next = p.next.next;
            self.s -= 1;
        
    def size(self): return self.s;
    
    def is_empty(self): return self.s == 0;

    def get(self,i):
        self.__assert_in_range(i,self.s-1);
        return self.node_at(i).element;
    
    def node_at(self,i):
        c = self.header
        for k in range(-1,i): c = c.next;
        return c;
    
    def contains(self,obj):
        self.__assert_not_none(obj);
        c = self.header.next;
        while(c != None and c.element != obj): c = c.next;
        return c != None;

    def append(self,obj):
        self.add(self.s,obj);
    
    def add(self,i,e):
        self.__assert_not_none(e);
        self.__assert_in_range(i,self.s);
        c = self.node_at(i-1);
        c.next = self.LinkedNode(e,c.next);
        self.s += 1;

    def pop(self,i=-1):
        if(i == -1): i = self.s-1;
        c = self.node_at(i-1);
        if(c != None): self.__rm_after(c);

    def remove(self,obj):
        self.__assert_not_none(obj);
        c = self.header
        while(c.next != None and c.next.element != obj): c = c.next;
        self.__rm_after(c);

    def set(self,i,obj):
        self.__assert_in_range(i,self.s-1);
        c = self.node_at(i);
        if(c != None): c.element = obj;
        
  
x = SLLWH();
x.add(0,"A");
x.append("B");
x.add(0,"C");
x.set(2,"D");
x.pop(1);
for i in range(x.size()): print(x.get(i));


class DBLinkedListWH:
    class LinkedNode:
        def __init__(self,e,p,n):
            self.element,self.prev,self.next = e,p,n;
    s = 0;
    def __init__(self): 
        self.header = self.LinkedNode(None,None,None);
        self.header.next = self.header.prev = self.header;

    def __assert_not_none(self,obj):
        assert(not(obj == None)),"None is not allowed"

    def __assert_in_range(self,i,m):
        assert(not(i < 0 or i > m)),"i must ∈ [0,self.size()-1]"

    def __node_at(self,i):
        c = self.header;
        for k in range(-1,i): c = c.next;
        return c;

    def __node_of(self,obj):
        c = self.header.next;
        while(c != self.header and c.element != obj): c = c.next;
        return c;
    
    def __add_before(self,n,obj):
        new_node = self.LinkedNode(obj,n.prev,n);
        n.prev.next = n.prev = new_node;
        self.s += 1;

    def __remove_node(self,node):
        p = node.prev; n = node.next;
        p.next = n; n.prev = p;
        self.s -= 1;

    def remove(self,e):
        self.__assert_not_none(e);
        n = self.__node_of(e);
        if(n != self.header): self.__remove_node(n);

    def pop(self,i=-1):
        if(i == -1): i = self.s -1;
        self.__assert_in_range(i,self.s-1);
        n = self.__node_at(i);
        self.__remove_node(n);
    
    def get(self,i):
        self.__assert_in_range(i,self.s-1);
        return self.__node_at(i).element;

    def append(self,obj): self.__add_before(self.header,obj)

    def add(self,i,e):
        self.__assert_in_range(i,self.s);
        self.__assert_not_none(e);
        n = self.__node_at(i);
        self.__add_before(n,e);

    def size(self): return self.s;

    def is_empty(self): return self.s == 0;

    def contains(self,obj):
        self.__assert_not_none(obj);
        return self.__node_of(obj) != self.header;

    def set(self,i,obj):
        self.__assert_in_range(i,self.s-1);
        self.__assert_not_none(obj);
        n = self.__node_at(i); n.element = obj;

x = DBLinkedListWH();
x.add(0,"A");
x.append("B");
x.add(0,"C");
x.set(2,"D");
x.pop(1);
for i in range(x.size()): print(x.get(i));



class SparseVector:
    class Element:
        def __init__(self,i,v):
            self.index,self.value = i,v;

    s = 0;
    def __init__(self,m):
        self.length = m;
        self.data = np.zeros(1,object);
    
    def size(self): return self.s;

    def __ensure_cap(self,m):
        if(m >= self.length):
            m = np.zeros(len(self.data)*2,object);
            for i in range(self.s): m[i] = self.data[i];
            self.data = m; self.length = len(m);

    def __assert_is_num(self,n):
        assert(type(n) == float or type(n) == int),"input must be float or int !"

    def __assert_in_range(self,i):
        assert(not(i < 0 or i > self.length)),"index out of range !"

    def get(self,i):
        self.__assert_in_range(i,self.length-1)
        for k in range(self.size):
            if(self.data[k].index == i): return self.data[k].value;
        else: return 0.0;

    def set(self,i,v):
        self.__assert_in_range(i);
        self.__assert_is_num(v); k = 0;
        while(k < self.size and self.data[k].index != i): k += 1;
        if(k < self.size): self.data[k].value = v;
        else: self.add(i,v);
    
    def add(self,i,e):
        if(e != 0.0):
            self.__assert_is_num(e);
            self.__assert_in_range(i);
            self.__ensure_cap(self.s);
            for k in range(self.s,i-1,-1): self.data[k] = self.data[k-1];
            self.data[i] = self.Element(i,e);
            self.s += 1;
    

    

    
    
    


































