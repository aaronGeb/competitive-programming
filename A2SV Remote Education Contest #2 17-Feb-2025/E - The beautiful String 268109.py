# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

import sys

def count_initial_1100(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i] == '1' and s[i+1] == '1' and s[i+2] == '0' and s[i+3] == '0':
            count += 1
    return count

def update_count(s, index, v, count_1100):
    affected_indices = range(max(0, index - 3), min(len(s) - 3, index + 1))  # Corrected range
    
    # Remove old occurrences
    for i in affected_indices:
        if s[i] == '1' and s[i+1] == '1' and s[i+2] == '0' and s[i+3] == '0':
            count_1100 -= 1

    s[index] = v  # Apply the change

    # Add new occurrences
    for i in affected_indices:
        if s[i] == '1' and s[i+1] == '1' and s[i+2] == '0' and s[i+3] == '0':
            count_1100 += 1

    return count_1100

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    result = []
    
    for _ in range(t):
        s = list(data[index])  # Read string as list
        index += 1
        q = int(data[index])
        index += 1

        count_1100 = count_initial_1100(s)

        for _ in range(q):
            i, v = data[index], data[index + 1]
            index += 2
            i = int(i) - 1  # Convert to 0-based index

            if s[i] != v:
                count_1100 = update_count(s, i, v, count_1100)

            result.append("YES" if count_1100 > 0 else "NO")

    sys.stdout.write("\n".join(result) + "\n")  # Efficient output

if __name__ == "__main__":
    main()