N = int(input())
mem = list(map(int, input().split()))
mem.sort()

result = 0
count = 0

#이미 정렬 되어있다는거 이용해서
#max 값 찾는 로직 필요없음. 지금 보는게 제일 높은 공포도
for i in mem:
    count+=1
    #== 여도 문제는 없을 듯
    if (count >= i):
        result += 1
        count = 0

print(result)