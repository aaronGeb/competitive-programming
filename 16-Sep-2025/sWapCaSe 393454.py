# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)