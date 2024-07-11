class Warior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} is sleeping')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} is eating')
        self.power += 2

    def hit(self):
        print(f'{self.name} is hitting')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} is walking')

    def info(self):
        print(f'Name: {self.name}, power: {self.power}, endurance: {self.endurance},'
              f' hair_color: {self.hair_color}')
        