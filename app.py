import characters
import random


class Simulator:
    def __init__(self):
        self.classes = [characters.Barbarian, characters.Elf,
                        characters.Wizard, characters.Dragon, characters.Knight]
        self.character_set = [self.generate_characters() for i in range(10)]
        self.display_character_set()

    def generate_characters(self):
        return random.choice(self.classes)()

    def display_character_set(self):
        for character in self.character_set:
            character.display_stats()

    def show_menu(self):
        pass


def main():
    Simulator()


if __name__ == "__main__":
    main()
