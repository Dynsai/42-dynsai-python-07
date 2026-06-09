from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex0.factory import CreatureFactory

def test_ex0(factory: CreatureFactory) -> None:
    print("=== Testing ex0 ===")
    new_creature = factory.create_base()
    print(f"{new_creature.describe()}")
    print(f"{new_creature.attack()}")
    print()
    evolved_creature = factory.create_evolved()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")


def battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print("=== FIGHT! ===")
    print(f"{creature_a.describe()}\nvs\n{creature_b.describe()}\n")
    print(f"{creature_a.attack()}")
    print(f"{creature_b.attack()}")


if __name__ == "__main__":
    heal_production = HealingCreatureFactory()
    transform_production = TransformCreatureFactory()

    test_ex0(heal_production)
    print()
    test_ex0(transform_production)
    print()
    battle(heal_production, transform_production)
    print()
    print("=== End of Program ===")


# TODO need to create all the prints and test on this file. 
# TODO so it does the same output as expected.