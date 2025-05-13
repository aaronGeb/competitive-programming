# Problem: Sort a Stack using Recursion - https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

def sorted_insert(s, x):
    if not s or x > s[-1]:
        s.append(x)
        return
    temp = s.pop()
    sorted_insert(s, x)
    s.append(temp)


def sort(s):
    if s:
        x = s.pop()
        sort(s)
        sorted_insert(s, x)


if __name__ == '__main__':
    s = []

    s.append(11)
    s.append(2)
    s.append(32)
    s.append(3)
    s.append(41)

    sort(s)

    while s:
        print(s.pop(), end=' ')
    print()