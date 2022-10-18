
from objects.HtmlAttribute import HtmlAttribute, HtmlAttributeType
from objects.HtmlElement import HtmlElement
from objects.HtmlElementType import HtmlElementType


class HtmlElementFactory():

    def __init__(self, elementType: str, id: str):
        self.elementType = elementType
        self.id = id

    def createElement(self):

        if self.elementType == "Etiqueta":
            return HtmlElement(self.id, HtmlElementType.LABEL, [
                HtmlAttribute(HtmlAttributeType.TEXT, "")
            ])

        elif self.elementType == "Boton":
            return HtmlElement(self.id, HtmlElementType.BUTTON, [
                HtmlAttribute(HtmlAttributeType.TEXT, "")
            ])

        elif self.elementType == "Check":
            return HtmlElement(self.id, HtmlElementType.CHECKBOX, [
                # HtmlAttribute(HtmlAttributeType.TEXT, ""),
                HtmlAttribute(HtmlAttributeType.IS_CHECKED, False)
            ])
        elif self.elementType == "RadioBoton":
            return HtmlElement(self.id, HtmlElementType.RADIOBUTTON, [
                # HtmlAttribute(HtmlAttributeType.TEXT, ""),
                HtmlAttribute(HtmlAttributeType.IS_CHECKED, False),
                HtmlAttribute(HtmlAttributeType.GROUP, "")
            ])
        elif self.elementType == "Texto":
            return HtmlElement(self.id, HtmlElementType.TEXT, [
                HtmlAttribute(HtmlAttributeType.TEXT, "")
            ])
        elif self.elementType == "AreaTexto":
            return HtmlElement(self.id, HtmlElementType.TEXTAREA, [
                HtmlAttribute(HtmlAttributeType.TEXT, "")
            ])
        elif self.elementType == "Clave":
            return HtmlElement(self.id, HtmlElementType.PASSWORD, [
                HtmlAttribute(HtmlAttributeType.TEXT, "")
            ])
        elif self.elementType == "Contenedor":
            return HtmlElement(self.id, HtmlElementType.DIV)

        else:
            return None
