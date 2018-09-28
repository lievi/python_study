""" Exercise for praticing OOP on python with a pokemon game"""

from random import randint
from typing import List


class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Pokemon(Player):
    def __init__(self, name: str, age: int, power: str, level: int = 1):
        super().__init__(name, age)
        self.level = level
        self.power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, new_power):
        self._power = new_power

    def attack(self):
        print("The {} is attacking".format(self.name))

    def evolve(self, new_name: str, new_power: str = None):
        if new_power is None:
            print("{} is evolving to {}".format(self.name, new_name))
        else:
            print("{} is evolving to {}. The power has changed to {}".format(
                self.name, new_name, new_power))
            self.name = new_name
            self.power = new_power
            self.level += 1


class Trainer(Player):
    def __init__(self, name: str, age: int, pokemons: List[Pokemon]):
        super().__init__(name, age)
        self.pokemons = pokemons
        self.names = []

    def catch(self, pokemon: Pokemon):
        print('Trying to catch the {}'.format(pokemon.name))
        # rolling the dice
        dice = randint(0, 1)
        if dice == 0 and pokemon.name != "Pikachu":
            print('{} miss the chance to catch a {}, try again, you need\n'
                  'to catch them all by the way'.format(
                      self.name, pokemon.name))
        else:
            self.pokemons.append(pokemon)
            print('Yeah, you catch the {}, they was added to your pokedex'.
                  format(pokemon.name))

    def show_pokemons(self):
        print("Showing all pokemons...")
        for pokemon in self.pokemons:
            print("Name: {} - level: {}".format(pokemon.name, pokemon.level))


ash = Trainer("Ash", 14, [])
pikachu = Pokemon("Pikachu", 9, power="eletric")
bulbasar = Pokemon("Bulbasar", 6, power="bug", level=2)
charizard = Pokemon("Charizard", 13, power="fire")

ash.catch(pikachu)
ash.catch(bulbasar)
ash.catch(charizard)

ash.show_pokemons()

pikachu.evolve("Raichu", "Eletric Master")
ash.show_pokemons()