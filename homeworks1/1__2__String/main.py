import re


def iscontact(string):
        if string.rfind("@") < string.rfind(".") and string.rfind("@") != -1 and string.rfind(".") != -1 \
                and string.count("@") == 1:
            return True
        else:
            return False


def isurl(string):
    word = string.split("://")
    if len(word) == 2:
        if len(word[0]) > 0 and len(word[1]) > 0:
            return True
    else:
        return False


def is_number(string):
    if len(string) > 3 and string.isdigit():
        return True
    else:
        return False

print("Введите строку")
string = input()
string = string.capitalize() 
list_words = string.split(" ")
# Переменные типа name1 - ОЧЕНЬ плохо
list_words1 = string.split(" ")  # Зачем?
new_str = ""
new_str1 = ""  # Зачем?

# Замена контактов с пом. встроенных функций
for i in range(0, len(list_words)):
    if iscontact(list_words[i]):
        list_words[i] = "[Контакты запрещены]"
new_str1 = re.sub(r'\w+(@)\w+\.\w+', " [Контакты запрещены] ", string)

# Замена ссылок с пом. встроенных функций
for i in range(0, len(list_words)):
    if isurl(list_words[i]):
        list_words[i] = "[ССылки запрещены]"
new_str2 = re.sub(r'\w+(://)\w+', " [ССылки запрещены] ", new_str1)

# Замена слов длиной больше 3 символов где все цифры с пом. встроенных функций
new_list = []
for i in range(0, len(list_words)):
    if not is_number(list_words[i]):
        new_list.append(list_words[i])

for word in new_list:
    new_str += word + " "
new_str3 = re.sub(r'(\d){3,}', "", new_str2)

print("фстроенные функции: ", new_str)
print("Регулярные выражения: ", new_str3)


"""
PEP8 - прочесть, запомнить, использовать всегда и везде:
https://drive.google.com/file/d/0B7cDWj1-Z0r0MmYwZjJhZWEtMjk1Zi00NWE5LWEzNTQtOTFjNjcwYjdhMGRl/view?ddrp=1&hl=ru#

Разбей код на модули (функции, классы)

__name__=='__main__'

Ознакомься со всеми встроенными функциями python для строк, и перепиши код под них
"""