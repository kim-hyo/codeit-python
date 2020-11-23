def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 코드를 쓰세요.
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)



natural = 0
while natural <= 100:
    if (natural%12 != 0):
        print(natural)
    natural += 8



count = 0
sum_num = 0
while count < 1000:
    if (count%2 == 0) or (count%3 == 0):
        sum_num += count
    count += 1
print(sum_num)


cnt = 1
NUM = 120
total = 0
while cnt <= NUM:
    if NUM%cnt == 0:
        total += 1
        print(cnt)
    cnt += 1
print(f"{NUM}의 약수는 총 {total}개입니다.")



NOW = 1989
FUTURE = 2016
MONEY = 50000000
EUNMA = 1100000000
deposit = 0
while NOW <= FUTURE:
    MONEY *= 1.12    
    NOW += 1    
if MONEY > EUNMA:
    print(f"{MONEY-EUNMA:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print(f"{EUNMA-MONEY:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.")


before = 1
more_before = 1
current = 1
count_num = 1
while (count_num <= 50):
    if (count_num <= 2):
        print(current)
    else:
        current = before + more_before
        print(current)
        more_before = before
        before = current
        
    count_num += 1


num_main = 1
while num_main <= 9:
    num_sub = 1
    while num_sub <= 9:
        print(f"{num_main} * {num_sub} = {num_main*num_sub}")
        num_sub += 1
    num_main += 1
