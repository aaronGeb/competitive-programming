# Problem: Check if a string is a scrambled form of another string - https://www.geeksforgeeks.org/check-if-a-string-is-a-scrambled-form-of-another-string/

def isAnagram(s1, s2):
    cnt = [0] * 26
    for ch in s1:
        cnt[ord(ch) - ord('a')] += 1
    for ch in s2:
        cnt[ord(ch) - ord('a')] -= 1

    for i in range(26):
        if cnt[i] != 0:
            return False
    return True

def isScramble(s1, s2):
  
    if len(s1) != len(s2):
        return False

    n = len(s1)

    if n == 0:
        return True
    if s1 == s2:
        return True
    if not isAnagram(s1, s2):
        return False

    for i in range(1, n):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
            return True
        if isScramble(s1[:i], s2[n - i:]) and isScramble(s1[i:], s2[:n - i]):
            return True
    return False
