with open('vocabulary.txt', 'r', encoding='UTF-8') as voc:
    for kor_eng in voc:
        question = kor_eng.split(": ")
        answer = input(f"{question[1].strip()}: ")
        if answer == question[0]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {question[0]}입니다.")
