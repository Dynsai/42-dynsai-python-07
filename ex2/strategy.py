from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(f"{creature.attack()}")
        else:
            raise ValueError("ERROR: Invalid creature for this strategy")

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            creature_transform = cast(TransformCapability, creature)
            print(creature_transform.transform())
            print(creature.attack())
            print(creature_transform.revert())
        else:
            raise ValueError("ERROR: Invalid creature for this strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            creature_heal = cast(HealCapability, creature)
            print(creature.attack())
            print(creature_heal.heal())
        else:
            raise ValueError("Invalid creature for this strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
