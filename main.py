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
            print ("Found pattern at index " + str(i-j)) 
            j = lps[j-1] 
  
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
KMPSearch(pat, txt) 
