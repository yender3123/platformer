class Hero:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1

    def hello(self):
        print('Привет я ' + self.name)

hero1 = Hero('Paladin')
hero1.hello()
hero2 = Hero('Warrior')
hero2.hello()