if []:
    print('[]은 True입니다.')
if [1, 2, 3]:
    print('[1, 2, 3]은 /True입니다.')
if {}:
    print('{}은 True입니다.')
if {'abc':1}:
    print("{'abc':1}은 True입니다.")
if 0:
    print('0은 True입니다.')
if 1:
    print('1은 True입니다.')

#두 번째 실습
a = 1 or 10
b = 0 or 10

print("a:{}, b:{}".format(a, b))