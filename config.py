import os
from typing import Dict, Any

BOT_TOKEN: str = "ВАШ_TELEGRAM_BOT_TOKEN"


GAME_CONFIG: Dict[str, Any] = {
    "default_hp": 100,        
    "default_gold": 50,       
    "xp_per_level": 100,
    "max_inventory_size": 20, 
}

ASSETS_PATHS: Dict[str, str] = {
    "texts": "assets/texts/",
    "images": "assets/images/",
}

LOGGING_CONFIG: Dict[str, Any] = {
    "level": "INFO", 
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "filename": "rpg_bot.log", 
}

ADMINS: list[int] = [123456789, 987654321]

DEBUG: bool = True 