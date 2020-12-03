# 첫 번째 실습
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

red_colors = rainbow[0: 4]
print(red_colors)

blue_colors = rainbow[4: 7]
print(blue_colors)

# 두 번째 실습
def substring(s, start, end):
    return s[start:end]


str = "Hello world"
between_2_5 = substring(str, 2, 5)
print(between_2_5)
