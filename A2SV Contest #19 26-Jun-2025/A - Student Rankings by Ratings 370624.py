# Problem: A - Student Rankings by Ratings - https://codeforces.com/gym/617023/problem/A

n = int(input())
ratings = list(map(int, input().split()))

indexed_ratings = [(rating, i) for i, rating in enumerate(ratings)]


indexed_ratings.sort(reverse=True)

positions = [0] * n
current_position = 1

for i, (rating, index) in enumerate(indexed_ratings):
    if i > 0 and rating == indexed_ratings[i - 1][0]:
        positions[index] = positions[indexed_ratings[i - 1][1]]
    else:
        positions[index] = i + 1


print(' '.join(map(str, positions)))