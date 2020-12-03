alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])


str_1 = 'Hello'
str_2 = ' World'

str_3 = str_1 + str_2

print(str_3)


list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

list_3 = list_1 + list_2

print(list_3)


# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    result = 0
    for i in str(num):
        result += int(i)
    return result


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
result = 0
for cnt in range(1, 1001):    
    result += sum_digit(cnt)

print(result)




def mask_security_number(security_number):
    # 코드를 입력하세요.
    secure_list = []
    result_str = ''
    for cnt in security_number:
        secure_list.append(cnt)
    for cnt in range(1, 5):
        secure_list[-cnt] = '*'
    for cnt in secure_list:
        result_str += cnt
    return result_str


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))



def is_palindrome(word):
    # 코드를 입력하세요.
    revesed_word = ''
    for cnt in range(1, len(word)+1):
        revesed_word += word[-cnt]
    return(word == revesed_word)


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))