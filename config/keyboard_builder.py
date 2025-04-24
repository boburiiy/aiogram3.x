from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    ReplyKeyboardBuilder,
    KeyboardBuilder,
)
from aiogram.types import (
    KeyboardButton,
    InlineKeyboardButton
)

from aiogram.utils.keyboard import ButtonType

from typing import Optional, Type

class kb_builder():
    keyboards = {
        'inline': {},
        'reply': {}
    }

    def __init__(self, name: Optional[str] = None):
        self.name = name

    @staticmethod
    class Create(KeyboardBuilder):
        def __init__(
            self,
            markup: list[list[ButtonType]],
            name: str,
        ):
            self.min_width = 1
            self.max_width = 10
            self.max_buttons = 100
            
            button_type = markup[0][0]
            kb_type = 'inline' if isinstance(
                button_type, InlineKeyboardButton) else "reply"
            
            button_type = button_type.__class__
            
            kb_builder.keyboards[kb_type][name] = self
            super().__init__(button_type=button_type, markup=markup)

    def get(self, name: str, kb_type: str = 'reply') -> Optional[Type[KeyboardBuilder]]:
        kb = kb_builder.keyboards.get(kb_type, {}).get(name)
        if kb is None:
            raise ValueError(
                f"No keyboard found with name '{name}' and type '{kb_type}'")
        return kb.as_markup()

    @staticmethod
    def kb_list():
        return kb_builder.keyboards