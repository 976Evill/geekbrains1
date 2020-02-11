# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Пишем ручкой Паркер')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Рисуем красным карандашом')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Маркер замечателен')


a = Stationery('Образец')
a.draw()
b = Pen('хорошая ручка Паркер')
b.draw()
c = Pencil('Красный карандаш')
c.draw()
d = Handle('Зелёный маркер ')
d.draw()
