

from typing import List
from objects.CssAttribute import CssAttribute
from objects.HtmlAttribute import HtmlAttribute, HtmlAttributeType
from objects.HtmlElementType import HtmlElementType


class HtmlElement():

    def __init__(self, id: str, tag: HtmlElementType, attributes: List[HtmlAttribute] = [], styles: List[CssAttribute] = []):
        self.id = id
        self.tag = tag
        self.attributes = attributes
        self.styles: List[CssAttribute] = []
        self.children: List[HtmlElement] = []

    def addChild(self, child):
        self.children.append(child)

    def setAtribute(self, attribute: HtmlAttribute):
        for atr in self.attributes:
            if attribute.type == atr.type:
                self.attributes.remove(atr)
                self.attributes.append(attribute)
                return True

        print("Atributo no encontrado !!!")
        return False

    def applyStyle(self, style: CssAttribute):
        for stl in self.styles:
            if style.type == stl.type:
                self.styles.remove(stl)
                self.styles.append(style)
                return True
        self.styles.append(style)

    def getAttribute(self, type: HtmlAttributeType):
        for atr in self.attributes:
            if atr.type == type:
                return atr.value
