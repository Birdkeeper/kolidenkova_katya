import urllib.request
from xml.etree import ElementTree

print("Введите код валюты")
valuta = input()
err = True

url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req"
file = urllib.request.urlopen(url)
fileParse = ElementTree.parse(file)

valuta = valuta.upper()
for line in fileParse.findall("Valute"):
    CharCode = line.find("CharCode").text
    if CharCode == valuta:
        rub = line.find("Value").text
        name = line.find("Name").text
        print("Курс ", name, " = ", rub, "рублей")
        err = False

if err == True:
    print("Код валюты не найден")
