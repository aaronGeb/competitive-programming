# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

def beautiful_matrix():
    matrix = [list(map(int, input().split())) for _ in range(5)]

    # Find the position of '1'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                row, col = i + 1, j + 1  
    moves = abs(row - 3) + abs(col - 3)

    print(moves)


if __name__ == "__main__":
    beautiful_matrix()
