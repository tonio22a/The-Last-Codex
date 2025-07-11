from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class GameObject:
    id: str
    name: str
    description: str

@dataclass
class Interactive(GameObject):
    is_interactable: bool = True

@dataclass
class Location(GameObject):
    connections: Dict[str, str]
    objects: List[Interactive] = None
    npcs: List['NPC'] = None
    enemies: List['Enemy'] = None

@dataclass
class Character(Interactive):
    hp: int
    max_hp: int
    dialogue: Optional[str] = None

@dataclass
class NPC(Character):
    quests: List['Quest'] = None
    faction: Optional[str] = None

@dataclass
class Enemy(Character):
    level: int
    damage: int
    loot_table: List['Item'] = None

@dataclass
class Item(GameObject):
    is_takable: bool = True
    value: int = 0

@dataclass
class Equipment(Item):
    slot: str  
    stats: Dict[str, int] = None 

@dataclass
class Consumable(Item):
    effects: Dict[str, int] = None

@dataclass
class Quest(GameObject):
    objectives: List[str]
    reward_xp: int
    reward_gold: int
    reward_items: List[Item] = None
    required_level: int = 1

@dataclass
class QuestProgress:
    quest_id: str
    completed: bool = False
    current_step: int = 0