# dictionary

my_dictionary = {
    5: 25, 
    2: 4,
    3: 9
}

my_family = {
    '아빠': '짱구아빠',
    '엄마': '짱구엄마',
    '짱구': '신짱구'
}

print(type(my_dictionary))
print(my_dictionary[3])
my_dictionary[9] = 81

print(my_family['아빠'])

vocab = {
    # 코드를 입력하세요.
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
}
print(vocab)


# 2. 새로운 단어들 추가
# 코드를 입력하세요.
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)


print(my_family.values())
print('짱구아빠' in my_family.values())
for i in my_family.values():
    print(i)
for j in my_family.keys():
    print(j)
for k, v in my_family.items():
    print(k, v)


# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    # 코드를 입력하세요.
    for key, value in dict.items():
        new_dict[value] = key
    
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    # 코드를 작성하세요.
    if name in vote_counter.keys():
        vote_counter[name] += 1
    else:
        vote_counter[name] = 1
    

# 후보별 득표수 출력
print(vote_counter)