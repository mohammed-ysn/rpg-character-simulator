import characters
import random


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

    def display_character_set(self):
        for character in self.character_set:
            character.display_stats()

    def main_menu(self):
        try:
            print('-' * 20)
            print('Menu')
            print('-' * 20)
            print('1) Display characters')
            print('2) Edit characters')
            print('3) Export characters')
            print('4) End program\n')
            option = int(input('Option (1-4): '))
            if option == 1:
                print('In progress')
            elif option == 2:
                print('In progress')
            elif option == 3:
                print('In progress')
            elif option == 4:
                self.show_menu_again = False
            else:
                raise ValueError
        except ValueError:
            print('You entered an invalid option.\n')


def main():
    Simulator()


if __name__ == "__main__":
    main()
