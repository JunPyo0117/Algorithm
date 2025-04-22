import math


def snail():
    # 올라가야할 거리 % 하루에 갈 수 있는 거리 ==0 낮 동안에 정상까지 감감
    # 올라가야할 거리 % 하루에 갈 수 있는 거리 !=0 낮 동안에 정상까지 가지 못해서 밤에 미끄러졌다는 뜻
    a, b, v = map(int, input().split())
    days = (v - b) / (a - b)

    # 실수면 올림처리 하여 날짜 계산산
    print(math.ceil(days))


snail()