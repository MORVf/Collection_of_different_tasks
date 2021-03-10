# Напишите скрипт на bash, который принимает на вход один аргумент (целое число от 0 до бесконечности), 
# который будет обозначать число студентов в аудитории. В зависимости от значения числа нужно вывести 
# разные сообщения.

#!/usr/bin/bash

if [[ $1 -eq 0 ]]
then
    echo "No students"
elif [[ $1 -eq 1 ]]
then
    echo "$1 student"
elif [[ $1 -ge 2 && $1 -le 4 ]]
then
    echo "$1 students"
else
    echo "A lot of students"
fi
