import random
import characters


class Simulator:
    def __init__(self):
        self.classes = [characters.Barbarian, characters.Elf,
                        characters.Wizard, characters.Dragon, characters.Knight]
        self.character_set = [self.generate_characters() for i in range(10)]
        self.show_menu_again = True
        while self.show_menu_again:
            self.main_menu()

    def generate_characters(self):
        return random.choice(self.classes)()

    def display_menu(self):
        print('\n' + '-' * 20)
        print('Menu')
        print('-' * 20)
        print('1) Display characters')
        print('2) Edit characters')
        print('3) Export characters')
        print('4) End program')

    def main_menu(self):
        try:
            self.display_menu()
            option = int(input('\nOption (1-4): '))
            if option == 1:
                for character in self.character_set:
                    character.display_stats()
            elif option == 2:
                print()
                for i, character in enumerate(self.character_set):
                    print('{}) {}'.format(i + 1, character.name))
                option = int(input('\nOption (1-10): '))
                if not 1 <= option <= 10:
                    raise ValueError
                self.character_set[option - 1].display_stats()
                attribute = input('\nAttribute to edit: ').lower()
                value = input('\nNew value: ')
                if attribute in ['health', 'power', 'special attack power', 'speed']:
                    int(value)
                attribute = {'type': 'character_type',
                             'health': 'health',
                             'power': 'power',
                             'special attack power': 'sp_attack_power',
                             'speed': 'speed'}[attribute]
                setattr(self.character_set[option - 1],
                        attribute, value)
            elif option == 3:
                print('\nOption in progress')
            elif option == 4:
                self.show_menu_again = False
            else:
                raise ValueError
        except ValueError:
            print('\nInvalid input.')


def main():
    Simulator()


if __name__ == "__main__":
    main()
