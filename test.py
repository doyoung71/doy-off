def solution(v):
    x=v[0][0]^v[1][0]^v[2][0]
    y=v[0][1]^v[1][1]^v[2][1]

    return [x, y]

print(solution([[1,4],[8,4],[8,50]]))