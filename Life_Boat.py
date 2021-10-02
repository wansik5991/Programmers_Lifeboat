import os
os.system('cls')

def solution(people, limit):
    people.sort()

    answer = 0
    front, end = 0, len(people)-1
    
    while True :
        answer += 1
        weight = people[end]
        end -= 1

        if weight + people[front] <= limit :
            front += 1
        if end < front : break;
    return answer

print(solution([40, 50, 60, 90], 100))
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([100,500,500,900,950], 1000))