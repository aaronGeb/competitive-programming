# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == "insert":
            i, e = int(command[1]), int(command[2])
            my_list.insert(i, e)
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif cmd == "append":
            e = int(command[1])
            my_list.append(e)
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()