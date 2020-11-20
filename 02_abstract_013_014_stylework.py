def is_evenly_divisible(number):
    return number%2 == 0
    # 코드를 작성하세요


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))



def calculate_change(payment, cost):
    change = payment - cost    
    fifty_thousand = int(change/50000)
    rest_change = change - (fifty_thousand*50000)
    ten_thousand = int(rest_change/10000)
    rest_change -= ten_thousand*10000
    five_thousand = int(rest_change/5000)
    rest_change -= five_thousand*5000
    one_thousand = int(rest_change/1000)
    print(f"50000원 지폐: {fifty_thousand}장")
    print(f"10000원 지폐: {ten_thousand}장")
    print(f"5000원 지폐: {five_thousand}장")
    print(f"1000원 지폐: {one_thousand}장")
    # 코드를 작성하세요.


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)