import re
import sys

def search_expression(string):
    """
    Ищет арифметическое выражение в строке
    :param string: исходная строка,в которой ищем выражение
    :return: список арифметических выражений
    """
    return re.findall(r'\d+[\.]*\d*[/+\-*]\d+[\.]*\d*', string)


def evaluate_expressions(list_expression):
    """
    Считает арифметическое выражение
    :param list_expression: список арифметических выражений, которые нужно посчитать
    """
    for expression in list_expression:
        print(expression, " = ", eval(expression))

if __name__ == '__main__':
    for string in sys.argv[1:]:
        list_expression = search_expression(string)
        evaluate_expressions(list_expression)






