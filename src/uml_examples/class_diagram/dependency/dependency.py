"""Пример взаимодействия объектов классов - зависимость."""


class Monitor:
    """Класс реализует взаимодействие с монитором"""

    def turn_on(self):
        """Включить монитор"""
        print("monitor is turned on")

    def turn_off(self):
        """Выключить монитор"""
        print("monitor is turned off")


class PowerSwitch:
    """Класс показывает, включено питание или нет"""

    def __init__(self):
        self.is_on = False

    def toggle(self, power_switch: Monitor):
        """Переключить состояние"""
        if self.is_on:
            power_switch.turn_off()
            self.is_on = False
        else:
            power_switch.turn_on()
            self.is_on = True

if __name__ == "__main__":
    monitor = Monitor()
    switch = PowerSwitch()
    switch.toggle(monitor)
