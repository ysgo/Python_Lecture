area_code = {
    '서울' : '02'
}
area_code['경기도']='031'
print(area_code)

for key in area_code:
    print(key)
    print(area_code[key])

for key, value in area_code.items():
    print(key)
    print(area_code[key])

for value in area_code.values():
    print(value)
