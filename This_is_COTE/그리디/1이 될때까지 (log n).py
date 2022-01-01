N,K = map(int,input().split())
count = 0

while(N!=1):
    #target은 K로 나누어 떨어지는 수
    target = (N//K)*K
    count += (N-target)
    N = target
    #N을 K로 더 나눌 수 없음
    if (N < K):
        break
    count += 1
    N //= K

#N 다 빼면 0됨
count += (N-1)
print(count)