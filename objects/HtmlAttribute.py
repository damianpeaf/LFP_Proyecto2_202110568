
from enum import Enum, auto
from typing import List


class HtmlAttributeType(Enum):
    TEXT = auto()
    VALUE = auto()
    IS_CHECKED = auto()
    GROUP = auto()


class HtmlAttribute():

    def __init__(self, type: HtmlAttributeType, value: List):
        self.type = type
        self.value = value
