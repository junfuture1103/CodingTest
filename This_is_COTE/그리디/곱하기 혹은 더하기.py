import re

#문자열 형태로 숫자 읽어서 요소하나씩 추출
input_string = input()
numbers = re.findall(r'\d', input_string)

#문자인 숫자들을 int형으로 변환
numbers = list(map(int, numbers))
result = 0
print(numbers)

#result가 1보다 작아도 더해야되네
#암튼 두 수중에 하나라도 1보다 작으면 더해줘야됨 ex) 1*4 < 1+4 / 5*1 < 5+1
for num in numbers:
    if (num == 0 or num == 1):
        print(num)
        result+=num
    else:
        if(result == 0):
            result+=num
            continue
        result*=num
print(result)