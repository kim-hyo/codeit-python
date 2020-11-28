numbers = [2, 3, 4, 5, 6, 7]
print(numbers[2:])
print(numbers[1:2])
print(numbers[:6])

print(numbers[-2:])



numbers = []
print(len(numbers))

numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))

del numbers[0]
print(numbers)

numbers.insert(2, 55)
print(numbers)