N = int(input())
mem = list(map(int, input().split()))

mem.sort()

left = 0
right = 0
count = 0

#max값 초기화
max = mem[0]
while(True):
    if(max <= right-left+1):
        count += 1
        left = right+1
        right = right+1
        if(right >= N):
            break
        #max 초기화
        max = mem[left]
    else:
        right+=1
        if(right >= N):
            break
        if(max < mem[right]):
            max = mem[right]
    
print(N, mem)
print(count)