import random

rand_num = random.randint(1, 20)
flag = 1

for cnt in range(4):
    entered_num = int(input("기회가 "+str(4-cnt)+"번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if entered_num == rand_num:
        print(f"축하합니다. {cnt+1}번 만에 숫자를 맞히셨습니다.")
        flag = 0
        break
    elif entered_num < rand_num:
        print("Up")
    else:
        print("Down")

if flag == 1:
    print(f"아쉽습니다. 정답은 {rand_num}였습니다.")
