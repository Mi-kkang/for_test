def get_money(day, N, sol, money) :
    global max_money
    if day == N :
        if max_money < money :
            max_money = money
    else :
        if sol == 0 and day + arr[0][day] <= N :
            get_money(day+1, N, arr[0][day]-1, money+arr[1][day])
        if sol - 1 <0 :
            sol = 1
        get_money(day+1, N, sol-1, money)


N = int(input())        # 퇴사까지 남은 시간
arr = [[0]*N for _ in range(2)]

for i in range(N) :
    day, pay = map(int,input().split())

    arr[0][i] = day
    arr[1][i] = pay

max_money = 0

get_money(0, N, 0, 0)

print(max_money)
