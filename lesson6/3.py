# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, income={}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


b = Worker('Anna', 'Glebko', 'ingeneer', {'wage': 128000, 'bonus': 60000})
print(b._income)


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(self.surname + ' ' + self.name)

    def get_total_income(self):
        print(sum(self._income.values()))


c = Position('Anna', 'Glebko', 'ingeneer', {'wage': 128000, 'bonus': 60000})
d = Position('Anton', 'Lebedev', 'ingeneer', {'wage': 123000, 'bonus': 80000})
c.get_full_name()
c.get_total_income()
d.get_full_name()
d.get_total_income()
