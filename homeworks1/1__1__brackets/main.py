import sys


def is_brackets_type_match(opening_bracket, closing_brackets):
    """
    Проверка на соврадение типов открывающихся и закрывающихся скобок
    :param opening_bracket: открывающаяся скобка
    :param closing_brackets: закрывающаяся скобка
    :return: bool
    """
    dict_brackets = {'{': '}', '[': ']', '(': ')'}
    if closing_brackets == dict_brackets[opening_bracket]:
        return True
    else:
        return False


def check_the_brackets(list_of_brackets):
    """
    Проверяет правильность расставления скобок в строке
    :param list_of_brackets: список скобок из строки
    """
    err = False
    index = 0

    open_brackets = []
    for bracket in list_of_brackets:
        if bracket == "{" or bracket == "[" or bracket == "(":
            open_brackets.append(bracket)
        else:
            if len(open_brackets) <= 0:
                err = True
                break
            elif is_brackets_type_match(open_brackets[len(open_brackets)-1], bracket):
                open_brackets.pop(len(open_brackets)-1)
            else:
                err = True
                break
        index += 1

    if index != len(list_of_brackets) and err:
        print(index+1)
    elif index == len(list_of_brackets) and len(open_brackets) == 0:
        print("yes")
    else:
        print("-1")

if __name__ == '__main__':
    for string in sys.argv[1:]:
        brackets = []
        for line in string:
            if line == "{" or line == "}" or line == "[" or line == "]" or line == "(" or line == ")":
                brackets.append(line)
        if len(brackets) == 0:
            print("Brackets not found")
        else:
            check_the_brackets(brackets)


'''
python main.py ")(" -> yes. Нужна защита от дурака". тут у меня выдает верный ответ (1), хотя я ничего не меняла
 в логике
'''
