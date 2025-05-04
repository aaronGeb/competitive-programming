# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def rremove(s):
    sb = ""
    n = len(s)
    i = 0
    while i < n:
        repeated = False
             while i + 1 < n and s[i] == s[i + 1]:
            repeated = True
      
            i += 1

      
        if not repeated:
            sb += s[i]
        i += 1

 
    if n == len(sb):
        return sb
 
    return rremove(sb)

s = "geeksforgeek"
result = rremove(s)
print(result)