def W(d,s,n):
    if(n <= 0): return [];
    minW = None; mn = 1e10; 
    for i in range(n):
        if(s[i:n+1] in d):
            words = W(d,s,i-1);
            if(words != None):
                words.append(s[i:n+1]);
                if(len(words) < mn): mn = len(words); minW = words; 
    return minW;

def ans(d,s): n = len(s); k = SeptWord(d,s); print(">>Input : ",s);print(">>Valid words\n",d); n = W(d,s,n); print(">>Minimum seperation\n",n);

#Dynamic Programing;
def SeptWord(d,s):
    n = k = len(s); M = [1e6 for _ in range(n+1)];I = [0 for _ in range(n)]; M[0] = 0; ans = [];
    for k in range(1,n):
        for i in range(k):
            if(s[i:k+1] in d and M[i-1] + 1 < M[k] ):  M[k] = M[i-1] + 1; I[k] = i;
    while(k >= 0):
        ans.insert(0,s[I[k] - 1 :k]); k = k - I[k] - 1;
    return ans;
    
d = set(); l = "The thunder under us to confirm thunderous roar ear he co firmed er of the jet over head confirmed her worst fear".split(" "); 
for e in l: d.add(e);
s = "Thethunderousroarofthejetoverheadconfirmedherworstfear"; ans(d,s);





