def backtraking(index, core, chip):
    global max_install, min_line
    # 최대설치의 최소라인수 구하기
    if index == depth:
        if max_install > core:
            return
        line = 0
        for i in range(n):
            for j in range(n):
                if chip[i][j] == 2:
                    line = line + 1
        if max_install == core:
            if line < min_line:
                min_line = line
        if max_install < core:
            min_line = line
            max_install = core
        return
    # 지금거 설치 안되는 경우 다음거 설치하려고 반복문 돌림
    for idx in range(index, depth):
        x, y = cores[idx]
        for d in range(4):
            xx = x
            yy = y
            install_list = []
            install = False
            while True:
                nx = xx + dx[d]
                ny = yy + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if chip[nx][ny] == 0:
                        xx, yy = nx, ny
                        install_list.append([xx, yy])
                    # 중간에 뭐 있는 경우
                    else:
                        break
                # 전선이 끝까지 도달한 경우 => 중간에 뭐 있는경우 없었음 => 설치가능
                else:
                    install = True
                    break
            if install:
                for ix, iy in install_list:
                    chip[ix][iy] = 2
                backtraking(idx + 1, core + 1, chip)
                for ix, iy in install_list:
                    chip[ix][iy] = 0


T = int(input())
for t in range(T):
    n = int(input())
    chip_origin = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_install, min_line = 0, int(1e9)
    cores = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if chip_origin[i][j] == 1:
                cores.append([i, j])
    depth = len(cores)
    backtraking(0, 0, chip_origin)
    print("#{} {}".format(t + 1, min_line))