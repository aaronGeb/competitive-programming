# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

def find_working_buttons(t, test_cases):
    result = []

    for s in test_cases:
        working = set()
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            count = j - i
            if count % 2 == 1:
                working.add(s[i])
            i = j

        result.append("".join(sorted(working)))

    return result


if __name__ == "__main__":
    t = int(input())
    test_cases = [input().strip() for _ in range(t)]
    answers = find_working_buttons(t, test_cases)
    for res in answers:
        print(res)
