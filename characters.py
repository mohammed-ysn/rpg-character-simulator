import random


class Character:
    def __init__(self, character_type, power, sp_attack_pwer, speed):
        self.name = self.generate_name()
        self.character_type = character_type
        self.health = 100
        self.power = power
        self.sp_attack_pwer = sp_attack_pwer
        self.speed = speed

    def generate_name(self):
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvxz'
        new_name = ''
        for i in range(3):
            for j in range(3):
                new_name += random.choice(consonants if j % 2 == 0 else vowels)
            new_name += '-' if i != 2 else ''
        return new_name


class Barbarian(Character):
    def __init__(self):
        super(Barbarian, self).__init__('Barbarian', 70, 20, 50)


class Elf(Character):
    def __init__(self):
        super(Elf, self).__init__('Elf', 30, 60, 10)


class Wizard(Character):
    def __init__(self):
        super(Wizard, self).__init__('Wizard', 50, 70, 30)


class Dragon(Character):
    def __init__(self):
        super(Dragon, self).__init__('Dragon', 90, 40, 50)


class Knight(Character):
    def __init__(self):
        super(Knight, self).__init__('Knight', 60, 10, 60)
