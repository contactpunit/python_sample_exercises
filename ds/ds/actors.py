import random


class Creatures:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return 'A {} of level {}'.format(self.name, self.level)

    def defensive_roll(self):
        role = random.randint(1, 12)
        return role * self.level


class Dragon(Creatures):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name=name, level=level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def defensive_roll(self):
        value = super().defensive_roll()
        value = value * self.scaliness
        if self.breathes_fire:
            value = value * 2
        return value


class Wizard(Creatures):
    def attack(self, creature):
        wizard_role = self.defensive_roll()
        creature_role = creature.defensive_roll()
        return wizard_role > creature_role
