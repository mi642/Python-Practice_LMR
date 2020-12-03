# 첫 번째 실습
a_list = [1, 2, 3, 4]
n = int(input())

def safe_index1(a_list, value):
    if value in a_list:
        return a_list.index(value)
    else:
        return None

def safe_index2(a_list, value):
    try:
        return a_list.index(value)
    except ValueError:
        return None

print(safe_index1(a_list, n))
print(safe_index2(a_list, n))

# 두 번째 실습
list = [1, 2, 3, 4]

list.insert(0, 8)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
