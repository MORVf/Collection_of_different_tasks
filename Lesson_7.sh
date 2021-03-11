# Напишите скрипт на bash, который будет определять в какую возрастную группу попадают пользователи. При 
# запуске скрипт должен вывести сообщение "enter your name:" и ждать от пользователя ввода имени. Когда имя 
# введено, то скрипт должен написать "enter your age:" и ждать ввода возраста. Когда возраст введен, скрипт 
# пишет на экран "<Имя>, your group is <группа>", где <группа> определяется на основе возраста по следующим правилам:
# 1) младше либо равно 16: "child",
# 2) от 17 до 25 (включительно): "youth",
# 3) старше 25: "adult".
# После этого скрипт опять выводит сообщение "enter your name:" и всё начинается по новой. Если в какой-то момент 
# работы скрипта будет введено пустое имя или возраст 0, то скрипт должен написать на экран "bye" и закончить свою работу.

#!/usr/bin/bash

while true
do
    echo "enter your name:"
    read name

    if [[ "$name" == "" ]]
    then
        echo "bye"
        break
    fi

    echo "enter your age:"
    read age

    if [[ $age -eq 0 ]]
    then
        echo "bye"
        break
    elif [[ $age -le 16 ]]
    then
        group="child"
    elif [[ $age -ge 17 && $age -le 25 ]]
    then
        group="youth"
    else
        group="adult"
    fi

    echo "$name, your group is $group"
done
