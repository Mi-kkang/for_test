def find_num(target, n) :
    dir = 0     # 오른쪽인지 왼쪽인지 위치를 확인하기 위한 변수 / 오른쪽이면 1, 왼쪽이면 -1이 될 예정
    start = 0
    end = n-1
    # mid = (start + end) // 2

    while True :
        mid = (start + end) // 2
        if A[mid] == target :
            return 1
        elif A[mid] < target :
            if dir == 1 :
                return 0
            # elif A[end] < target :
            #     return 0
            # elif A[end] == target :
            #     return 1
            else :
                dir = 1
                start = mid + 1
        else :
            if dir == -1 :
                return 0
            # elif A[start] > target :
            #     return 0
            # elif A[start] == target :
            #     return 1
            else :
                dir = -1
                end = mid - 1
    return 0

t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # 서로 다른 정수 N(A에 저장될 예정) / 리스트 B에 저장된 M개의 정수
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()

    cnt = 0

    for i in range(M) :
        cnt += find_num(B[i],N)

    print(f'#{tc} {cnt}')