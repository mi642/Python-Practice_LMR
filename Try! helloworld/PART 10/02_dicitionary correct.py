#첫 번째 실습
days_in_month = {'1월':31, '2월':28, '3월':31}
days_in_month['2월'] = 29

print(days_in_month['2월'])

#두 번째 실습 - del
days_in_month = {'1월':31, '2월':28, '3월':31, '-1월':97889789}
del(days_in_month['-1월'])

print(days_in_month)

#두 번째 실습 - pop
days_in_month = {'1월':31, '2월':28, '3월':31, '-1월':97889789}
days_in_month.pop('-1월')

print(days_in_month)