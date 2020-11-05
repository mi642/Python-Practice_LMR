#첫 번쨰 실습
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3
list3 = [1, 2, 3]
tuple3 = tuple(list3)

if tuple1 == tuple2 == tuple3:
    print('모두 같음')

#두 번쨰 실습
tuple1 = (11, 22, 33)
for i in range(len(tuple1)):
    print(tuple1[i])