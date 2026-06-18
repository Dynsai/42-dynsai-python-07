from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def test_heal() -> None:
    print("=== Testing healing ===")
    factory = HealingCreatureFactory()
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


def test_transform() -> None:
    print("=== Testing transform ===")
    factory = TransformCreatureFactory()
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
    test_heal()
    print()
    test_transform()
    print("=== End of Program ===")
