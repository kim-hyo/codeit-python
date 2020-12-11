import random

def generate_numbers(n):
    lotto_num = []
    cnt = 0
    while cnt != n:
        l_num = random.randint(1, 45)
        if l_num in lotto_num:            
            continue
        else:
            lotto_num.append(l_num)
            cnt += 1
    return lotto_num

def draw_winning_numbers():
    winning_list = sorted(generate_numbers(6))
    dup = True
    while dup != False:
        num = random.randint(1, 45)
        if num in winning_list:
            dup = True
        else:
            winning_list.append(num)
            dup = False
    return winning_list

def count_matching_numbers(list_1, list_2):
    cnt = 0
    for i in list_1:
        if i in list_2:            
            cnt += 1        
    return cnt

def check(numbers, winning_numbers):
    isBonus = False

    for i in numbers:
       if i == winning_numbers[-1]:
           isBonus = True        
            
    get_num = count_matching_numbers(numbers, winning_numbers)
    if get_num == 6 and not isBonus:
        return 1000000000
    elif get_num == 6 and isBonus:
        return 50000000
    elif get_num == 5 and not isBonus:
        return 1000000
    elif get_num == 4 and not isBonus:
        return 50000
    elif get_num == 3 and not isBonus:
        return 5000
    else:
        return 0
