num = str(input('Введите 1, если хотите использовать заданный в коде массив\n'
                'Введите любой символ, отличный от 1, если хотите ввести массив с клавиатуры: '))

if num == '1':
    entered_list = ['hello', '2', 'world', ':-)']
else:
    entered_list = list(map(str, input("Введите элементы массива разделенные пробелом: ").split()))


def less_four(en_list):
    res = []
    for i in en_list:
        if len(i) <= 3:
            res.append(i)
    return res


res_list = less_four(entered_list)
print(entered_list, '->', res_list)