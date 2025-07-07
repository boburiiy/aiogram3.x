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
    # documentation crated by ai just because developer is lazy
    """
    kb_builder is a class for managing and storing keyboard layouts for aiogram bots.
    Attributes:
        keyboards (dict): A class-level dictionary storing created keyboards, separated by type ('inline' or 'reply').
    Methods:
        __init__(self, name: Optional[str] = None):
            Initializes a kb_builder instance with an optional name.
            A static inner class for creating and registering new keyboard layouts.
            Args:
                markup (list[list[ButtonType]]): The keyboard layout as a list of button rows.
                name (str): The name to register the keyboard under.
            Attributes:
                min_width (int): Minimum width of the keyboard.
                max_width (int): Maximum width of the keyboard.
                max_buttons (int): Maximum number of buttons allowed.
            Registers the keyboard in the kb_builder.keyboards dictionary under the appropriate type ('inline' or 'reply').
        
	get(self, name: str, kb_type: str = 'reply') -> Optional[Type[KeyboardBuilder]]:
            Retrieves a registered keyboard by name and type.
            Args:
                name (str): The name of the keyboard to retrieve.
                kb_type (str): The type of keyboard ('inline' or 'reply'). Defaults to 'reply'.
            Returns:
                Optional[Type[KeyboardBuilder]]: The keyboard markup if found.
            Raises:
                ValueError: If the keyboard with the specified name and type is not found.
        kb_list():
            Returns the dictionary of all registered keyboards.
            Returns:
                dict: The keyboards dictionary containing all registered keyboards by type and name.
    """
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

