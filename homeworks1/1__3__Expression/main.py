import re

print("input string")
string1 = input()
string = ""

for i in range(0, len(string1)):
    if string1[i] != " ":
        string += string1[i]

word = ""
words = []
i = 0

while i != len(string):
    if re.match(r'(-?\d+((\.)|(,))?\d*?[/+\-*]?)+', string[i:]) != None:
        word = re.match(r'(-?\d+((\.)|(,))?\d*[/+\-*]?)+', string[i: ]).group()
        words.append(word)
        i += int(re.match(r'(-?\d+((\.)|(,))?\d*[/+\-*]?)+', string[i: ]).end())
    else:
        i += 1
word1= ''
for i in range(0, len(words)):
    str = words[i]
    if not str[len(str)-1].isdigit():
        words[i] = str[: len(str)-1]

for str in words:
    print(str, " = ", eval(str))

"""
Модули в коде!

Докстринги

циклы по строкам пиши с помошью for symbol in string, а не while цикла =)

Строки для тестирования лучше принимать в качестве аргументов командной строки
(argparse библиотека), а не через input().
Так удобней, не надо строку каждый раз вводить руками



python main.py
input string
84*54 фыва 99-65 54/3

84*54  =  4536
99-6554/3  =  -2085.6666666666665 - Это явно неверный результат

"""

