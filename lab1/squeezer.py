class Squeezer:
    comparing_number = 0
    change_number = 0

    def __init__(self, name, color, max_juice_level, power_consumption, producer):
        self.name = name
        self.color = color
        self.max_juice_level = max_juice_level
        self.power_consumption = power_consumption
        self.producer = producer

    def __repr__(self):
        return str(self.name) + "--> " + str(self.color) + "--> " + str(self.max_juice_level) + " litres/hour --> " + str(
            self.power_consumption) + " kW -->" + str(self.producer) + "\n"

    # def print_list(self):
    #     for squeezer in squeezer_list:
    #         print(squeezer)

    @staticmethod
    def compare():
        Squeezer.comparing_number += 1
        return Squeezer.comparing_number

    @staticmethod
    def changes():
        Squeezer.change_number += 1
        return Squeezer.change_number

    @staticmethod
    def reset():
        Squeezer.comparing_number = 0
        Squeezer.change_number = 0