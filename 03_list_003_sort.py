numbers = [19, 13, 2, 5, 11]

new_list = sorted(numbers)
print(new_list)

new_list = sorted(numbers, reverse=True)
print(new_list)
print(numbers)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)



greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

cnt = 0
while (cnt < len(greetings)):
    print(greetings[cnt])
    cnt += 1


def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    return(round((((fahrenheit-32)*5)/9), 1))


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
cnt = 0
while (cnt < len(temperature_list)):
    temperature_list[cnt] = fahrenheit_to_celsius(temperature_list[cnt])
    cnt += 1
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력





# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 코드를 입력하세요.
    return (round(krw/1000, 1))


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 코드를 입력하세요.
    return (round(usd*(1000/8),1))


# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))
 
# amounts를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.
cnt = 0
while (cnt < len(amounts)):
    amounts[cnt] = krw_to_usd(amounts[cnt])
    cnt += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.
cnt = 0
while (cnt < len(amounts)):
    amounts[cnt] = usd_to_jpy(amounts[cnt])
    cnt += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))




# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
cnt = 0
while (cnt < len(numbers)):        
    if (numbers[cnt]%2 != 0):        
        del numbers[cnt]
    else:
        cnt += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)
