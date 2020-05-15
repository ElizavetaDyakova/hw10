# Предметная область – автосалон. Разработать класс CarDealership, описывающий работу автосалона.
# Разработать класс Car, автомобиль описывается следующими параметрами: уникальный идентификатор,
# марка автомобиля, страна-производитель, год выпуска, объем двигателя, стоимость.
# Разработать класс Lorry на базе класс Car, грузовик характеризуется: весовым ограничение перевозки.
#

from abc import ABCMeta, abstractmethod


#Метакласс описывающий работу автосалона
class CarDealership(metaclass=ABCMeta):

    def __init__(self, iden, mark, countr, year, v, stoim):
        self.iden = iden
        self.mark = mark
        self.countr = countr
        self.year = year
        self.v = v
        self.stoim = stoim

    @abstractmethod
    def info(self):
        pass

#класс машина
class Car(CarDealership):
    #вывод информации о машинах
    def info(self):
        print(f"Машина\nid:{self.iden}\n"
              f"Марка:{self.mark}\n"
              f"Страна-производитель: {self.countr}\n"
              f"Год выпуска: {self.year}"
              f"\nОбъем двигателя: {self.v}"
              f"\nСтоимость: {self.stoim}")


#класс грузовик
class Lorry(Car):
    __slots__ = ('iden', 'mark', 'countr', 'year', 'v', 'stoim', 'ogr')

    def __init__(self, iden, mark, countr, year, v, stoim, ogr):
        self.iden = iden
        self.mark = mark
        self.countr = countr
        self.year = year
        self.v = v
        self.stoim = stoim
        self.ogr = ogr

    def info(self):
        print(f"\nГрузовик\nid:{self.iden}"
              f"\nМарка:{self.mark}\n"
              f"Страна-производитель: {self.countr}\n"
              f"Год выпуска: {self.year}\n"
              f"Объем двигателя: {self.v}\n"
              f"Стоимость: {self.stoim}\n"
              f"Весовое ограничение "
              f"перевозки:{self.ogr}")


if __name__ == '__main__':
    cat = Car('125', 'Lamborgini', 'USA', '2002', '70л', '236748p')
    cat.info()
    lorry = Lorry('2849', 'Lamborgini', 'USA', '1999', '100л', '234648p', '1000кг')
    lorry.info()


