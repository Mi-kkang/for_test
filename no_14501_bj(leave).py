def get_money(day, money) :
    global max_money
    if day >= N or day + arr[0][day] >= N:
        if max_money < money :
            max_money = money
        return

    get_money(day+arr[0][day], money+arr[1][day])
    get_money(day+1,money)


N = int(input())        # 퇴사까지 남은 시간
arr = [[0]*N for _ in range(2)]

for i in range(N) :
    day, pay = map(int,input().split())

    arr[0][i] = day
    arr[1][i] = pay

max_money = 0

get_money(0,0)

print(max_money)
