#첫 번째 실습
sizes = [33, 35, 34, 37, 32, 39, 35, 29]

for i, size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i))
        break

#두 번째 실습
numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a, b, a / b))