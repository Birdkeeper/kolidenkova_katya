from math import sqrt


def read_file(file_name):
    """
    Чтение и обработка данных файла
    :param file_name: имя файла
    :return: список координат
    """
    f = open(file_name)
    list_of_coordinates = []
    for line in f:
        point = line.strip()
        new_list_of_coordinates = point.split(" ")
        if len(new_list_of_coordinates) == 2 and new_list_of_coordinates[0].isdigit() and \
                new_list_of_coordinates[1].isdigit():
            list_of_coordinates.append(new_list_of_coordinates)
    return list_of_coordinates


def distance(point1, point2):
    """
    Считает расстояние между двумя точками
    :param point1: список координат первой точки
    :param point2: список координат второй точки
    :return: расстояние между точками
    """
    x = abs(float(point1[0]) - float(point2[0]))
    y = abs(float(point1[1]) - float(point2[1]))
    return sqrt(x**2 + y**2)


def maximum_distance(list_of_coordinates):
    """
    Ищет наибольшее расстояние
    :param list_of_coordinates: список координат
    :return: максимальное расстояние
    """
    maximum = distance(list_of_coordinates[0], list_of_coordinates[1])
    for i in range(0, len(list_of_coordinates)):
        for j in range(i + 1, len(list_of_coordinates)):
            if maximum < distance(list_of_coordinates[i], list_of_coordinates[j]):
                maximum = distance(list_of_coordinates[i], list_of_coordinates[j])
    return maximum


def minimum_distance(list_of_coordinates):
    """
    Ищет минимальное расстояние между точками
    :param list_of_coordinates: список координат
    :return: минимальное расстояние
    """
    minimum = distance(list_of_coordinates[0], list_of_coordinates[1])
    for i in range(0, len(list_of_coordinates)):
        for j in range(i + 1, len(list_of_coordinates)):
            if minimum > distance(list_of_coordinates[i], list_of_coordinates[j]):
                minimum = distance(list_of_coordinates[i], list_of_coordinates[j])
    return minimum


if __name__ == '__main__':
    points = read_file('text4')
    if len(points) > 1:
        print("max = ", maximum_distance(points))
        print("min = ", minimum_distance(points))
    else:
        print("Error: Нужно минимум две точки")

