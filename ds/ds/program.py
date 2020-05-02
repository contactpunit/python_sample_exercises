from ds.ds.actors import Creatures, Wizard, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('-' * 12)
    print('      GAME PROGRAM      ')
    print('-' * 12)


def game_loop():
    creatures = [
        Creatures('Bat', 5),
        Creatures('Tiger', 12),
        Creatures('Toad', 1),
        Wizard('Evil wizard', 1000),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False)
    ]

    hero = Wizard('Gandalf', 75)
    while True:
        active_creature = random.choice(creatures)

        print('A {} of level {} has appeared'.format(active_creature.name, active_creature.level))
        print()
        cmd = input(' Do you [a]ttack, [r]un away or [l]ook around?: ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print('The wizard defeated {}'.format(active_creature.name))
            else:
                print('The wizard has been defeated by {}'.format(active_creature.name))
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            for c in creatures:
                print(" * {} of level {}".format(
                    c.name, c.level
                ))
        else:
            print('exiting .... bye')
            break

        print()


if __name__ == '__main__':
    main()
