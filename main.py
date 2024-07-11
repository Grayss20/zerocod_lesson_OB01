class Warrior():
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


war1 = Warrior('Nik', 10, 10, 'black')
war2 = Warrior('Egor', 20, 20, 'white')


print(war1.power)
war2.info()

war2.sleep()

war2.info()
