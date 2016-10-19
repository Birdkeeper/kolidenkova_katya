import re
import sys


def iscontact(string):
    """
    проверяет, является ли слово контактом
    :param string: слоо для проверки
    :return: bool
    """
    if string.rfind("@") < string.rfind(".") and string.rfind("@") != -1 and string.rfind(".") != -1 \
                and string.count("@") == 1:
        return True
    else:
        return False


def isurl(string):
    """
    проверяет, является ли слово ссылкой
    :param string: слово для проверки
    :return: bool
    """
    word = string.split("://")
    if len(word) == 2:
        if len(word[0]) > 0 and len(word[1]) > 0:
            return True
    else:
        return False


def is_number(string):
    """
    проверяет,я вляется ли слово числом более 3х символов
    :param string: слово для проверки
    :return: bool
    """
    if len(string) > 3 and string.isdigit():
        return True
    else:
        return False


def built_in_function(string):
    """
    изменяет слово
    :param string: слово из исходной строки
    :return: изменонное слово
    """
    if iscontact(string):
        string = "[Контакты запрещены]"
    elif isurl(string):
        string = "[ССылки запрещены]"
    elif is_number(string):
        string = ""
    return string


def built_in_regexp(string):
    """
    изменяет строку с пом. регулярных выражений
    :param string: исходная строка целиком
    :return: измененная строка
    """
    new_str1 = re.sub(r'\w+(@)\w+\.\w+', " [Контакты запрещены] ", string)
    new_str2 = re.sub(r'\w+(://)\w+', " [ССылки запрещены] ", new_str1)
    new_str3 = re.sub(r'(\d){3,}', "", new_str2)
    return new_str3

if __name__ == '__main__':
    for string in sys.argv[1:]:
        string = string.capitalize()
        list_words = string.split(" ")
        new_str = ""
        for word in list_words:
            word = built_in_function(word)
            new_str += word + " "
        print("Встроенные функции: ", new_str)
        print("Регулярные выражения: ", built_in_regexp(string))

