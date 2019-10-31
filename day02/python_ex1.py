import requests
import random

area_code = {
    '서울':'02'
}
area_code['경기도']='031'
# print(area_code)

'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
# print('==== Q1 ====')
sum = 0
for key in score:
    sum += score[key]
print(sum / len(score))

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 84,
        '국어': 90,
        '음악': 92
    },
    'b': {
        '수학': 83,
        '국어': 91,
        '음악': 77
    }
}

# 아래에 코드를 작성해 주세요.
# print('==== Q2 ====')
for value in scores.values():
    sum = 0
    for values in value.values():
        sum += values
    print(sum / len(value.values()))

total = 0
for i in scores['a']:
    total += scores['a'][i]
for j in scores['b']:
    total += scores['b'][j]
ave = total / (len(scores['a']) + len(scores['b']))
print(ave)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
for value in city.values():
    sum = 0
    #print(value)
    for values in value:
        sum += values
    print(sum / len(value))
    

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cnt = 0
for key, value in city.items():
    if cnt==0:
        hot = max(value)
        cold = min(value)
        hot_city = key
        cold_city = key
    else:
        if hot < max(value):
            hot = max(value)
            hot_city = key
        if cold > min(value):
            cold = min(value)
            cold_city = key
    cnt += 1
print(hot_city)
print(cold_city)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
if 2 in city['서울']:
    print('서울은 2도 였었던 적이 있습니다.')
else:
    print('서울은 2도인적이 없습니다.')