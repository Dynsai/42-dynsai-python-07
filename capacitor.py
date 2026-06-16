from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex1.factory import CreatureFactory


def test_heal(factory: CreatureFactory) -> None:
    print("=== Testing healing ===")
    new_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(f"{new_creature.describe()}")
    print(f"{new_creature.attack()}")
    print(f"{new_creature.heal()}")
    print()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.heal()}")
    print()


def test_transform(factory: CreatureFactory) -> None:
    print("=== Testing transform ===")
    new_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(f"{new_creature.describe()}")
    print(f"{new_creature.attack()}")
    print(f"{new_creature.transform()}")
    print(f"{new_creature.attack()}")
    print(f"{new_creature.revert()}")
    print()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.transform()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.revert()}")
    print()


if __name__ == "__main__":
    heal_production = HealingCreatureFactory()
    transform_production = TransformCreatureFactory()

    test_heal(heal_production)
    print()
    test_transform(transform_production)
    print("=== End of Program ===")
