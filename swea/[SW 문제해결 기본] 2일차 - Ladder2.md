```python
import copy

for _ in range(10):
    tc = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]
    x = 0
    y = 0
    start_x = []
    for idx in range(100):
        if box[y][idx]:
            start_x.append(idx)
    cnt_dict = {}
    for i in start_x:
        x = i
        y = 0
        two_box = copy.deepcopy(box)
        cnt = 0
        while y <= 99:
            if x == 0:
                if two_box[y][x + 1]:
                    two_box[y][x + 1] = 0
                    x += 1
                    cnt += 1

            elif x == 99:
                if two_box[y][x - 1]:
                    two_box[y][x - 1] = 0
                    x -= 1
                    cnt += 1
            if 99 > x > 0:
                if two_box[y][x - 1] or two_box[y][x + 1]:
                    if two_box[y][x - 1]:
                        two_box[y][x - 1] = 0
                        x -= 1
                        cnt += 1
                    elif two_box[y][x + 1]:
                        two_box[y][x + 1] = 0
                        x += 1
                        cnt += 1
            if y == 99:
                cnt_dict[cnt] = i
                break
            if y != 99 and two_box[y + 1][x]:
                two_box[y + 1][x] = 0
                y += 1
                cnt += 1
    a = min(cnt_dict.keys())
    print(f'#{tc} {cnt_dict[a]}')
```