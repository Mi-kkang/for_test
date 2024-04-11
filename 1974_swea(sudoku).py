def check_row(n) :
    global ans
    if ans == 0 :
        return
    for i in range(n) :
        num = []
        for j in range(n) :
            if puzzle[i][j] in num :
                ans = 0
                return
            else :
                num.append(puzzle[i][j])

def check_colum(n) :
    global ans
    if ans == 0 :
        return
    for j in range(n) :
        num = []
        for i in range(n) :
            if puzzle[i][j] in num :
                ans = 0
                return
            else :
                num.append(puzzle[i][j])

def check_box(n) :
    global ans
    if ans == 0 :
        return

    for i in range(0, n, 3) :
        for j in range(0, n, 3) :
            num = []

            for k in range(3) :
                for l in range(3) :
                    if puzzle[i+k][j+l] in num :
                        ans = 0
                        return
                    else :
                        num.append(puzzle[i+k][j+l])


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    n = 9
    puzzle = [list(map(int,input().split())) for _ in range(n)]
    ans = 1

    # 1) 가로를 확인해본다.
    check_row(n)

    # 2) 세로를 확인해본다.
    check_colum(n)

    # 3) 3x3 칸을 확인해본다.
    check_box(n)

    print(f'#{tc} {ans}')