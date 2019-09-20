# KMP-Algorithm
Python code for implementation of Knuth Morris Pratt(KMP) algorithm

## Intoduction
The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst case complexity to O(n). The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match.<br>

## About the code
The code here searches for a given string pattern in the given string

### Input
1. The text<br>
2. The pattern to be searched for in the text

### Output 
If the pattern is found it displays the index in the text at which it is found
