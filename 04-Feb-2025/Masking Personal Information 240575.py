# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name,domain = s.split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            digit = re.sub(r'\D','',s)
            local_number = '***-***-' + digit[-4:]
            if len(digit) ==  10:
                return local_number
            else:
                return f"+{'*' * (len(digit)-10)}-{local_number}"