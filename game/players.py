from classes import Character, Item, QuestProgress
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Dict, List

@dataclass
class PlayerClass(ABC):
    name: str
    description: str
    base_hp: int
    base_attack: int
    abilities: List[str]
    
    @abstractmethod
    def class_bonus(self, player: 'Player'):
        pass
    
    def __str__(self):
        return self.name    

@dataclass
class Warrior(PlayerClass):
    def __init__(self):
        super().__init__(
            name="",
            description="",
            base_hp=100,
            base_attack=10,
            abilities=[]
        )
    
    def class_bonus(self, player):
        return super().class_bonus(player)


@dataclass
class Player(Character):
    level: int = 1
    xp: int = 0
    inventory: List[Item] = None
    equipment: Dict[str, Item] = None
    gold: int = 0
    quests: List[QuestProgress] = None
    player_class: PlayerClass = None
    
    def set_class(self, player_class: PlayerClass):
        self.player_class = player_class
        self.max_hp = player_class.base_hp
        self.hp = player_class.base_hp
        self.attack = player_class.base_attack
        player_class.class_bonus(self)
        
    def use_ability(self, ability_index: int):
        if not self.player_class or ability_index >= len(self.player_class.abilities):
            return "Неверная способность"
        return f"Использовано: {self.player_class.abilities[ability_index]}"
