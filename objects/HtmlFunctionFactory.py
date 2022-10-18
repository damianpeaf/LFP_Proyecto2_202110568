
from typing import List
from lexer.Token import Token, TokenType
from objects.CssAttribute import CssAttribute, CssAttributeType
from objects.HtmlAttribute import HtmlAttribute, HtmlAttributeType


class HtmlFunctionFactory():

    def __init__(self, targetId: str, targetAttribute: str, params: List[Token]):
        self.targetId = targetId
        self.targetAttribute = targetAttribute
        self.params = params

    def _validateParams(self, types: List[TokenType]):
        numberOfParams = len(types)
        if len(self.params) != numberOfParams:
            return f"La funcion esperaba {str(numberOfParams)} parametro/s"

        for i in range(len(self.params)):
            if self.params[i].tokenType != types[i]:
                return f"El parametro {str(i + 1)} debe ser de tipo {types[i].name}"

        return True

    def applyFunction(self):
        # Search the target element
        from core.Core import Core

        targetElement = Core.getElement(self.targetId)
        targetAttribute: CssAttributeType | HtmlAttributeType = None

        if targetElement is None:
            return f"El elemento {self.targetId} no existe"

        # Search the target attribute
        if self.targetAttribute == 'setColorLetra':
            targetAttribute = CssAttributeType.COLOR
            validations = self._validateParams([TokenType.NUMBER, TokenType.NUMBER, TokenType.NUMBER])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setTexto':
            targetAttribute = HtmlAttributeType.TEXT
            validations = self._validateParams([TokenType.STRING])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setAlineacion':
            targetAttribute = CssAttributeType.ALIGNMENT

            validations = self._validateParams([TokenType.STRING])
            if validations != True:
                return validations

            if self.params[0].lexeme == '':
                self.params[0].lexeme = "Izquierdo"

            if self.params[0].lexeme not in ['Centro', 'Izquierdo', 'Derecho']:
                return "El parametro debe ser Centro, Izquierdo o Derecho"

        elif self.targetAttribute == 'setColorFondo':
            targetAttribute = CssAttributeType.BACKGROUNG_COLOR
            validations = self._validateParams([TokenType.NUMBER, TokenType.NUMBER, TokenType.NUMBER])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setMarcada':
            targetAttribute = HtmlAttributeType.IS_CHECKED
            validations = self._validateParams([TokenType.BOOLEAN])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setGrupo':
            targetAttribute = HtmlAttributeType.GROUP
            validations = self._validateParams([TokenType.STRING])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setAncho':
            targetAttribute = CssAttributeType.WIDHT
            validations = self._validateParams([TokenType.NUMBER])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setAlto':
            targetAttribute = CssAttributeType.HEIGHT
            validations = self._validateParams([TokenType.NUMBER])
            if validations != True:
                return validations

        elif self.targetAttribute == 'setPosicion':
            targetAttribute = CssAttributeType.POSITION
            validations = self._validateParams([TokenType.NUMBER, TokenType.NUMBER])
            if validations != True:
                return validations

        elif self.targetAttribute == 'add':
            validations = self._validateParams([TokenType.ID])
            if validations != True:
                return validations

            children = Core.getElement(self.params[0].lexeme)
            if children is None:
                return f"El elemento hijo {self.params[0].lexeme} no existe"

            targetElement.addChild(children)
            return True
        else:
            return "La funcion no existe"

        # clean the params
        params = None
        if len(self.params) > 1:
            params = []
            for param in self.params:
                params.append(param.lexeme)
        else:
            params = self.params[0].lexeme

        # execute the function
        if isinstance(targetAttribute, HtmlAttributeType):
            targetElement.setAtribute(HtmlAttribute(targetAttribute, params))
            return True

        elif isinstance(targetAttribute, CssAttributeType):
            targetElement.applyStyle(CssAttribute(targetAttribute, params))
            return True

        return "Hubo un error al ejecutar la funcion"
