for _ in range(10):
    tc = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]

    x = 0
    y = 99

    for idx in range(100): # 0 1 2 3 4 5 6 7 8 9
        if box[y][idx] == 2:
            x = idx # 2가 있는 x좌표 설정.

    while True: # < -
        if y == 0: # 도착했을때
            break

        if x == 0:
            if box[y][x+1] == 1: # 오른쪽 가는 동작
                box[y][x] = 0
                x += 1
            elif box[y-1][x] == 1: # 위로 가는 동작
                box[y][x] = 0
                y -= 1
        elif x == 9:
            if box[y][x-1] == 1:# 왼쪽 칸에 1이 있다면 왼쪽으로 한칸 이동
                box[y][x] = 0
                x -= 1
            elif box[y-1][x] == 1: # 위로 가는 동작
                box[y][x] = 0
                y -= 1
        else:
            if box[y][x-1] == 1:# 왼쪽 칸에 1이 있다면 왼쪽으로 한칸 이동
                box[y][x] = 0
                x -= 1
            elif box[y][x+1] == 1: # 오른쪽 가는 동작
                box[y][x] = 0
                x += 1
            if box[y-1][x] == 1: # 위로 가는 동작
                box[y][x] = 0
                y -= 1

    print(f'#{tc} {x}')

