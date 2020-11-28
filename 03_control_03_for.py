my_list = [2, 3, 5, 7, 11]

for num in my_list:
    print(num)



#for i in range(3, 11):
#    print(i)


#for i in range(10):
#    print(i)

for i in range(3, 17, 3):
    print(i)


numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 코드를 입력하세요.
index = 0
for i in numbers:
    print(f"{index} {i}")    
    index += 1


for i in range(11):
    result = 2 ** i
    print(f"2^{i} = {result}")


for primary in range(1, 10):
    for secondary in range(1, 10):
        print(f"{primary} * {secondary} = {primary*secondary}")


res = False
for a in range(1, 998):
    if res:
        break
    else:
        for b in range(a+1, 999):
            c = 1000-a-b
            if ((a*a)+(b*b)) == (c*c):
                res = True
                print(a*b*c)
                break


numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.
for i in range((int)(len(numbers)/2)):
    numbers[i], numbers[-i-1] = numbers[-i-1], numbers[i]

print("뒤집어진 리스트: " + str(numbers))