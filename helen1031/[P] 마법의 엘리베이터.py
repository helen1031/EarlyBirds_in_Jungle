def solution(storey):
    answer = 0

    while storey != 0:
        end = storey % 10
        storey = storey // 10

        if end >= 6 or (end >= 5 and storey % 10 >= 5):
            answer += 10 - end
            storey += 1

        else:
            answer += end

    return answer