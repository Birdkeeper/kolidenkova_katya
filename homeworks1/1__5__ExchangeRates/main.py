import urllib.request
from xml.etree import ElementTree
from datetime import date


def find_currency(currency_cod):
    """
    Ищет курс нужной валюты в рублях
    :param currency_cod: код валюты
    """
    err = True
    currency_cod = currency_cod.upper()
    for line in fileParse.findall("Valute"):
        CharCode = line.find("CharCode").text
        if CharCode == currency_cod:
            rub = line.find("Value").text
            name = line.find("Name").text
            print("Курс ", name, " = ", rub, "рублей")
            err = False
    if err:
        print("Код валюты не найден")


if __name__ == '__main__':
    print("Введите код валюты, для выхода нажмите 0")
    currency = input()
    while currency != '0':
        date_today = date.today().strftime("%d/%m/%Y")
        url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + date_today
        file = urllib.request.urlopen(url)
        fileParse = ElementTree.parse(file)
        find_currency(currency)
        print("Введите код валюты, для выхода нажмите 0")
        currency = input()


