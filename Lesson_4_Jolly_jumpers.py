'''
Последовательность n>0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей последовательных 
элементов принимают все возможные значения между 1 и n−1.
Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как абсолютные разности равны 
4 1 3 2, соответственно, а n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.
Формат ввода:
Строка, содержащая 1≤n≤10000 целых чисел, разделённых пробелом.
Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly" в противном случае.

Sample Input 1:
1 -3 -4 -1 1
Sample Output 1:
Jolly

Sample Input 2:
1 3 5
Sample Output 2:
Not jolly

Sample Input 3:
4
Sample Output 3:
Jolly
'''

sequence_in = input().split() #считываем строку и заполняем список подстроками

sequence_abs_diff = []    #список с элементами абсолютных разностей

def is_jolly(sequence):   #функция определения принадлежности переданной последовательности к jolly jumper
    temp_sequence = []    #упорядоченный список-jolly jumper
    for number in range(1, len(sequence_in)):   #генерируем список-jolly jumper
        temp_sequence += [number]

    if sequence_abs_diff == temp_sequence:   #если вычисленный список == сгенерированному списку-jolly jumper
        return print('Jolly')   #то возвращаем Jolly
    else:   #иначе
        return print('Not jolly')   #Not jolly

if len(sequence_in) == 1:   #если входящая последовательность состоит из одного элемента, то
    print('Jolly')   #сразу выводим Jolly
else:   #иначе
    for number1 in range(len(sequence_in) - 1):   #пробегаем все элементы списка
        number2 = number1 + 1
        while number2 < len(sequence_in):
            diff_numbers = abs(int(sequence_in[number1]) - int(sequence_in[number2]))   #из предыдущего элемента-числа списка вычитаем последующий и берём модуль разности
            sequence_abs_diff += [diff_numbers]    #накапливаем разности в специальном списке
            break   #завершаем цикл

    sequence_abs_diff.sort()   #сортируем полученный список по возрастанию
    is_jolly(sequence_abs_diff)   #вызываем функцию с полученным списком в качестве аргумента
