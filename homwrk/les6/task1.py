#. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    #атрибуты класса
    _color_r = 'красный'
    _color_y = 'желтый'
    _color_g = 'зеленый'

    #методы класс
    def time(self):
        TrafficLight.time_r = 7
        print(f'светофор переключается\n в {TrafficLight._color_r} \nосталось {TrafficLight.time_r} секунд ')
        TrafficLight.time_y = 2
        print(f'светофор переключается\n в {TrafficLight._color_y} \nосталось {TrafficLight.time_y} секунды ')
        TrafficLight.time_g = 5
        print(f'светофор переключается\n в {TrafficLight._color_g} \nосталось {TrafficLight.time_g} секунд ')





b = TrafficLight()
b.time()


        