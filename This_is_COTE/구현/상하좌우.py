n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for plan in plans:
    for i in range(len(move_types)):
        if (plan == move_types[i]):
            tmp_x = x+dx[i]
            tmp_y = y+dy[i]
            
    if (tmp_x < 1 or tmp_y <1 or tmp_x > n or tmp_y > n):
        continue

    x = tmp_x
    y = tmp_y
        
print(x, y)