def calculate_distance(now, number):
    dis = 0
    if now % 3 == 0 or now % 3 == 1:
        dis += 1
    dis += abs((now - 1) // 3 - (number - 1) // 3)
    return dis


def solution(numbers, hand):
    answer = ''
    l = 10
    r = 12
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            l = number
        elif number in [3, 6, 9]:
            answer += "R"
            r = number
        else:
            if number == 0:
                number = 11

            lefthand_distance = calculate_distance(l, number)
            righthand_distance = calculate_distance(r, number)
            if lefthand_distance > righthand_distance:
                answer += "R"
                r = number
            elif lefthand_distance < righthand_distance:
                answer += "L"
                l = number
            else:
                if hand == "left":
                    answer += "L"
                    l = number
                else:
                    answer += "R"
                    r = number

    return answer