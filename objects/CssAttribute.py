
from enum import Enum, auto
from typing import List


class CssAttributeType(Enum):
    BACKGROUNG_COLOR = auto()
    POSITION = auto()
    WIDHT = auto()
    HEIGHT = auto()
    ALIGNMENT = auto()
    COLOR = auto()


class CssAttribute():

    def __init__(self, type: CssAttributeType, value: List):
        self.type = type
        self.value = value
