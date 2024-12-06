def solution(people, limit):
    people.sort()
    boats= 0
    light = 0
    heavy = len(people) - 1

    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        boats += 1

    return boats

print(solution([70,50,80,50],100))
