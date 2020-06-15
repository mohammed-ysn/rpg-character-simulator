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

    def display_stats(self):
        print('-' * 20)
        print('{} stats'.format(self.name))
        print('-' * 20)
        print('Type: {}'.format(self.character_type))
        print('Health: {}'.format(self.health))
        print('Power: {}'.format(self.power))
        print('Special attack power: {}'.format(self.sp_attack_pwer))
        print('Speed: {}\n'.format(self.speed))

    def set_name(self, name):
        self.name = name

    def set_character_type(self, character_type):
        self.character_type = character_type

    def set_health(self, health):
        self.health = health

    def set_power(self, power):
        self.power = power

    def set_sp_attack_pwer(self, sp_attack_pwer):
        self.sp_attack_pwer = sp_attack_pwer

    def set_speed(self, speed):
        self.speed = speed


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


if __name__ == "__main__":
    print('Run app.py')
