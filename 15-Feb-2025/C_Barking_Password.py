def can_unlock(password, words):
    first, second = password 
 
    
    if password in words:
        return "YES"
 
   
    has_first = has_second = False
    for word in words:
        if word[1] == first:
            has_first = True
        if word[0] == second:
            has_second = True
        if has_first and has_second:
            return "YES"
    
    return "NO"
 
# Read input
password = input().strip()
n = int(input().strip())
words = {input().strip() for _ in range(n)} 
 
 
print(can_unlock(password, words))