# 첫 번째 실습
list = [0, 1, 2, 3, 4]
for a in range(0, 4):
    print(a)

# 두 번째 실습
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
for a in range(len(rainbow)):
    color = rainbow[a]
    print('{}번째 색은 {}'.format(a + 1, color))

# 세 번째 실습
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
for a, color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(a + 1, color))

# 네 번째 실습
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for a in range(12):
    month = days[a]
    print('{}월의 날짜 수는 {}일 입니다.'.format(a + 1, month))

for a in range(len(days)):
    month = days[a]
    print('{}월의 날짜 수는 {}일 입니다.'.format(a + 1, month))

for a, month in enumerate(days):
    print('{}월의 날짜 수는 {}일 입니다.'.format(a + 1, month))
