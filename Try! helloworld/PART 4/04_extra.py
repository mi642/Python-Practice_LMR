x, y = map(int, input().split())

def cal(x, y):
    return x + y, x - y, x * y, x / y

a, s, m, d = cal(x, y)
print("덧셈 : {}, 뺄셈 : {}, 곱셈 : {}, 나눗셈 : {}".format(a, s, m, d))