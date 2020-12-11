import random

def generate_numbers():
    numbers = []
    cnt = 0
    while cnt != 3:
        b_num = random.randint(0, 9)
        if b_num in numbers:            
            continue
        else:
            numbers.append(b_num)
            cnt += 1
    print(f"0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")    
    return numbers

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    
    for i in range(0, 3):
        if guess[i] in solution:
            if guess[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1
    
    return strike_count, ball_count


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    for i in range(1, 4):
        num = -1
        while num < 0 or num > 10:
            num = int(input(f"{i}번째 숫자를 입력하세요: "))
            if num in new_guess:
                print("중복되는 숫자입니다. 다시 입력하세요.")
                num = -1
                continue
            if num >= 0 and num < 10:
                new_guess.append(num)
            else:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
                num = -1        

    return new_guess


ANSWER = generate_numbers()
tries = 0
result = False

while not result:
    tries += 1
    strike, ball = get_score(take_guess(), ANSWER)
    print(f"{strike}S {ball}B")
    if strike == 3:        
        result = True
    