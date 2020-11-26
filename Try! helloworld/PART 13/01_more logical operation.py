dictionary = {'key2': 'value1'}

if 'key1' in dictionary:
    if dictionary['key1' == 'value1']:
        print('key1도 있고, 그 값은 value1이다.')
    else:
        print('1아니네')
else:
    print('2아니네')

dictionary = {'key2': 'value1'}

if 'key1' in dictionary and dictionary['key1' == 'value1']:
    print('key1도 있고, 그 값은 value1이다.')
else:
    print('3아니네')
