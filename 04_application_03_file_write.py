with open('new_file.txt', 'w') as f:
    f.write("Hello World\n")
    f.write("My name is Hyo")

with open('new_file.txt', 'a') as f:
    f.write("add the string")

loop = ''
with open('vocabulary.txt', 'w', encoding='UTF-8') as v:
    while loop != 'q':
        loop = input("영어 단어를 입력하세요: ")
        if loop == 'q':
            break
        v.write(loop+": ")        
        loop = input("한국어 뜻을 입력하세요: ")
        if loop == 'q':
            break
        v.write(loop+"\n")