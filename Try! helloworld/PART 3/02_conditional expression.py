#첫 번째 실습
from datetime import datetime
hour = datetime.now().hour

if hour<12:
    print('오전입니다.')

if hour>12:
    print('오후입니다.')

#두 번째 실습
number = 15
if number%3==0:
    print('{}는 3의 배수입니다.'.format(number))

number = 16
if number%3==0:
    print('{}는 3의 배수입니다.'.format(number))

#세 번째 실습
from datetime import datetime
hour = datetime.now().hour

if hour%6==0:
    print('종이 울립니다.')