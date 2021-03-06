from lps import computeLPSArray
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    lps = [0]*M 
    j = 0 
    computeLPSArray(pat, M, lps) 
  
    i = 0 
    while i < N: 
        if pat[j].lower() == txt[i].lower(): 
            i += 1
            j += 1
  
        if j == M: 
            return (i-j) 
            j = lps[j-1] 
  
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
 
