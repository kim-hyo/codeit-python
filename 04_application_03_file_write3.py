import random
my_vocabulary = {}
keys = []
with open('vocabulary.txt', 'r', encoding='UTF-8') as voc:
    for line in voc:
        line_split = line.strip().split(": ")
        temp_dict = {line_split[1]:line_split[0]}
        my_vocabulary.update(temp_dict)
        keys.append(line_split[1])
    answer = ''
    while answer != 'q':
        seq = random.randint(0, len(keys)-1)
        answer = input(f"{keys[seq]}: ")
        if answer == 'q':
            break
        if answer == my_vocabulary[keys[seq]]:
            print("맞았습니다!")
        else:
            print(f"틀렸습니다. 정답은 {my_vocabulary[keys[seq]]}입니다.")
