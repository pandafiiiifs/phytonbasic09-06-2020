#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.



class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return(f' {self.name} поехала')

    def stop(self):
        return(f'{self.name} остановилась')

    def turn_left(self):
        return(f'{self.name} повернула налево')

    def turn_right(self):
        return(f'{self.name} повернула направо')

    def show_speed(self):
        return(f'текущая скорость {self.name}\n{self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        self.is_police = True
        if self.is_police:
            return(f'{self.name} полицейская машина')
        else:
            return (f'{self.name} не полицейская машина')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def town_car_speed(self):
        if self.speed > 60:
            return(f'{self.name} превышение скорости!')
        else:
            return (f'{self.name} скорость в норме!')



class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def work_car_speed(self):
        if self.speed > 40:
            return (f'{self.name} превышение скорости!')
        else:
            return (f'{self.name} скорость в норме!')



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)





a = PoliceCar(100, 'черно-белая' , 'audi', True)
b = TownCar(62, 'красная' , 'volvo', False)
c = WorkCar(39, 'коричневая', 'KIA', False)
d = SportCar(110, 'желтая', 'Ferarri', False)
print(a.police())
print(a.show_speed())
print(b.town_car_speed())
print(c.work_car_speed())
print(d.go(),d.turn_left(), d.show_speed() , d.turn_right())