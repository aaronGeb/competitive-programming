# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

def second_min_names(data):
    unique_results = sorted(set(result for _, result in data))  
    if len(unique_results) < 2:
        return None  
    
    second_min = unique_results[1]  

    names = [name for name, result in data if result == second_min]
    for _ in sorted(names):
        print(_)

if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
           
            name = input()
            score = float(input())
            data.append([name, score])
second_min_names(data)
    