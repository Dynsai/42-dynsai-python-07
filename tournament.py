from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(combatants: List[Tuple[CreatureFactory,
                                  BattleStrategy]]) -> None:
    print(f"{len(combatants)} combatants involved")

    for i in range(len(combatants)):
        for j in range(i + 1, len(combatants)):
            factory_a, strategy_a = combatants[i]
            factory_b, strategy_b = combatants[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print()
            print("*** Battle ***")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print("## FIGHT! ##")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # Tournament 0: Ok strategies
    # Flameling with Normal vs HealingType with Defensive
    print("=== Tournament 0 ===")
    print("    Flameling with Normal vs HealingType with Defensive")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print()

    # Tournament 1: Incorrect strategies
    # Flameling with Aggressive vs HealingType with Defensive
    print("=== Tournament 1 (Incorrect strategies) ====")
    print("    Aquabub with Aggressive vs HealingType with Defensive")
    battle([
        (AquaFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print()

    # Tournament 2: All three strategies. All three ok.
    # Aquabub with Normal,
    # HealingType with Defensive,
    # TransformType with Aggressive
    print("=== Tournament 2 (Multiple strategies. All ok.) ===")
    print(
        "    Fireling+Normal vs Healing+Defensive vs Transform+Aggressive"
    )
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])
    print("=== End of Program ===")
