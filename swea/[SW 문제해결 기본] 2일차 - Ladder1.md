-   [S/W 문제해결 기본] 2일차 - Ladder1



-   ```python
    for test_case in range(1, 11):
        n = input()
        map_s = [list(map(int, input().split())) for _ in range(100)]
        x, y = map_s[99].index(2), 99
        while True:
            if x == 0:
                if map_s[y][x + 1]:
                    map_s[y][x + 1] = 0
                    x += 1
    
            elif x == 99:
                if map_s[y][x-1]:
                    map_s[y][x - 1] = 0
                    x -= 1
            if 99 > x > 0:
                if map_s[y][x-1] or map_s[y][x+1]:
                    if map_s[y][x-1]:
                        map_s[y][x - 1] = 0
                        x -= 1
                    elif map_s[y][x + 1]:
                        map_s[y][x + 1] = 0
                        x += 1
    
            if map_s[y-1][x]:
                map_s[y - 1][x] = 0
                y -= 1
            if y == 0:
                print(f'#{test_case} {x}')
                break
    ```