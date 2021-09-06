def lcs_slow(X,Y):
    n = len(X); m = len(Y);
    return lcsr1(X,Y,n-1,m-1);
    
def lcsr1(X,Y,i,j):
    if(i == -1 or j == -1): return 0;
    if(X[i] == Y[j]): return lcsr1(X,Y,i-1,j-1) + 1;
    return max(lcsr1(X,Y,i-1,j),lcsr1(X,Y,i,j-1));

#TopDown
def lcs_td(X,Y):
    n = len(X); m = len(Y);
    M = [[0 for _ in range(m)] for _ in range(n)];
    return lcsr2(X,Y,n-1,m-1,M)

def lcsr2(X,Y,i,j,M):
    if(i < 0 or j < 0): return 0;
    if(M[i][j] > 0): return M[i][j];
    if(X[i] == Y[j]):
        M[i][j] = lcsr2(X,Y,i-1,j-1,M) + 1;
    else:
        M[i][j] = max(lcsr2(X,Y,i-1,j,M),
                      lcsr2(X,Y,i,j-1,M));
    return M[i][j];


def lcs_bt(X,Y):
    n = len(X); m = len(Y);
    M = [[0 for i in range(m+1)] for _ in range(n+1)];
    D = [[0 for i in range(m)] for _ in range(n)];
    for i in range(n+1): M[i][0] = 0;
    for i in range(m+1): M[0][i] = 0;
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1] == Y[j-1]):
                M[i][j] = M[i-1][j-1] + 1; D[i-1][j-1] = "ud";
            elif M[i][j-1]>M[i-1][j] :
                M[i][j] = M[i][j-1]; D[i-1][j-1] = "<-";
            else: M[i][j] = M[i-1][j]; D[i-1][j-1] = "^";
    return (M,D);


def findLCS1(X,Y):
    M,D = lcs_bt(X,Y);n = len(X) -1; m = len(Y) -1
    lcs = "";i = n; j = m;
    while(i >= 0 and j >= 0):
        if(D[i][j] == "ud"):
            lcs = str(X[i]) + lcs; i -= 1; j-= 1;
        elif(D[i][j] == "<-"): j -= 1;
        else : i-= 1;
    print("Longest common sub DNA sequence is",lcs);print("with size",M[n+1][m+1]);
    return lcs;

def findLCS2(X,Y):
    M = lcs_bt(X,Y)[0]; n = len(X)-1; m = len(Y)-1;
    i = n; j = m; lcs = "";
    while(i >= 0 and j >= 0):
        if(X[i] == Y[j]): lcs = str(X[i]) + lcs; i -= 1; j-= 1;
        elif(M[i+1][j] > M[i][j+1]): j -= 1;
        else: i -= 1;
    print("Longest common sub DNA sequence is",lcs);print("with size",M[n+1][m+1]);
    return lcs
    
X = list("caaaacgatggatccgtccggcctctaaacgaacatagatacgggtccgataaagtaatgcgagatatcttggaaaagcatatcatgcgctaaggtaccccacggagctgagtactctattggggttctgctccatttgctaatactcacgtattatcagagatacaatacgtcaatattataagggatgcgacgggaacgcgaagcctgtacagttcgtgtgtccgggtgtccgtgttaggttagaactacagataatgggtatagccttcgaaaaccggagatctgggcaaacacggcaccccataggtcccgttagccagtagcttaaacgggtcccccgtatggtcttaacaagatattagtaaagtcaaagcttcatccttctgactctaaagtgcgtattgttgctgcgttggaggggatgaaattactcaataaagtgggttgctggaatgaatgcaagacttcctcctccccgtagtaattcaacacggacc");
Y = list('aaacttatagtccctgggtcgtaggagttactcgatagcaaaaaatacttcggaagttaacgtcgccaatacattgacgaatggtacctggcggtttgactgtaaaggtctcctgacgagacccggctcggagggtacggcattacgttcctatcctgcccaggcagaagactcagagtatagcgaacaaagacactatattgagtagcgcacaacatcagtccggcatagcgaaactaggaagtgttgtatctcgttagacataaccaaattgcagctcactctgatagtccatgcttaactcgagttggggccatcttcggcggcgtgacttggaagtaggtgggcctggaagcttacgcaccgatgtcatacttatttcatagcgggttgtggcccatggcgtagctatcacaaacttctggtgaagacgcttcctagatctgttgtgagacgttcttctattccatcgtcttgtgtgctcctgtacaagctagacctacggtaagcaaggctaaaccccagtacaaagtcgacggtcattgggcggcagatattcgcataatcctttacacgcaaaaagaaatgctatgtctaata')
#a1 = lcs_slow(X,Y);
a3 = findLCS1(X,Y);
a4 = findLCS2(X,Y);

