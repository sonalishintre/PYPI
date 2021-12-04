"""
Reverse the given string 
for example:  input python 
return nothyp
time comlexity O(N) 

"""

def reverse_string(s):
    r = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)


s = "sonali"
print(reverse_string(s))