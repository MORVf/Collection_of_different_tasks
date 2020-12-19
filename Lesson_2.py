'''
Напишите программу, имитирующую обработчик команд от пользователя.
Программа должна выводить оповещение о своём состоянии в следующем формате:
Когда пользователь вводит команду, содержимое которой обозначим как <command>, программа должна вывести фразу
Processing "<command>" command...
Например, пользователь ввёл Come to me, в таком случае должна быть выведена строка
Processing "Come to me" command...
Считывание команд должно продолжаться до ввода команды End, при этом программа должна вывести сообщение
Good bye!
и завершиться (см. пример).

Для считывания команд используйте функцию input без аргументов.

Формат ввода:
Последовательность команд, каждая на отдельной строке. Команда состоит из символов латинского алфавита, пробелов 
и символов табуляции. Гарантируется отсутствие пробельных символов в начале и конце строки. Последняя команда всегда End.

Формат вывода:
Сообщения об обработке команд, как указано в задании, по одному сообщению на строку.

Sample Input:
Turn left
Move forward
Turn left
Move forward
Turn left
Move forward
Turn left
Move forward
End

Sample Output:
Processing "Turn left" command...
Processing "Move forward" command...
Processing "Turn left" command...
Processing "Move forward" command...
Processing "Turn left" command...
Processing "Move forward" command...
Processing "Turn left" command...
Processing "Move forward" command...
Good bye!
'''

i = 0

while i >= 0: считываем строки в цикле
    command = input()
    if command != 'End': #если это не End, то
        print('Processing \"' + command + '\" command...') #выводим фразу
        i += 1  #продолжаем выполнять след. иттерацию цикла
    else:  #иначе выводим фразу
        print('Good bye!')
        break   #завершаем цикл
