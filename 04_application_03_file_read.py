daily_income = []
total_income = 0
days = 0
with open('chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        day_income = line.split()
        daily_income.append(day_income[1])
    for cnt in daily_income:
        total_income += int(cnt)
        days += 1
print(total_income/days)

print("     aaa      vvv     cccc     ".strip())
print("     \t    \n     aaa    bbbb    cccc \n\n\n".strip())


my_string = '1. 2. 3. 4. 5. 6'
print(my_string.split('.'))

full_name = 'Kim, Hyo'
name_data = full_name.split(', ')
last_name = name_data[0]
first_name = name_data[1]
print(first_name, last_name)

numbers = '    \n\n    2   \t    3 \n\n    5 7 11   \n\n'.split()
print(numbers)



