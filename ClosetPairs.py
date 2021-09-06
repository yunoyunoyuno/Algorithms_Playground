def bruteforceCS(P):
    n = len(P); m = 10**6;
    for i in range(n):
        for j in range(i+1,n):
            dx = abs(P[i][0] - P[j][0])
            dy = abs(P[i][1] - P[j][1]);
            d = (dx**2 + dy**2)**0.5
            if(d < m): m = d;
    return m;


P = [(3,2),(4,1),(-5,-2),(4,2),(0,10),(9,-1)];

ans = bruteforceCS(P);


