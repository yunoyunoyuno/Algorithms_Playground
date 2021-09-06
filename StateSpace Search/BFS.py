class State:
    def __init__(self,v,p,op):
        self.val = v;self.parent = p;self.op = op;

def ans(state,a):
    if(state == None): a.append("1"); return;
    a.append(state.op);
    ans(state.parent,a);
    return a;

def sol(a,ans):
    s = ""
    for e in a: s = e+s;
    return s + "="+str(ans);

def m3d2BFS(target):
    q = []; s = set();
    q.append(State(1,None,'*3'));
    while(len(q) > 0):
        state = q.pop(0);
        if(state.val == target): return ans(state.parent,[]);
        m3 = state.val*3
        if(not m3 in s):
            q.append(State(m3,state,"*3")); s.add(m3)
        d2 = state.val//2
        if(not d2 in s):
            q.append(State(d2,state,"/2")); s.add(d2)

s = m3d2BFS(41);
s = sol(s,41);
        
