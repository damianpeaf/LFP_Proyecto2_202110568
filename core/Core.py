from typing import List
from constants.idType import idType
from lexer.Lexer import Lexer
from lexer.Token import TokenType
from objects.HtmlElement import HtmlElement
from objects.HtmlElementFactory import HtmlElementFactory
from objects.HtmlElementType import HtmlElementType
from objects.HtmlFunctionFactory import HtmlFunctionFactory
from parser2.Parser import Parser


class Core():

    SymbolTable: List[HtmlElement] = []
    runTimeErrors = []

    def __init__(self):
        Core.SymbolTable = []
        Core.runTimeErrors = []

        if len(self.getErrors()) != 0:
            return

        self.createSymbolTable()
        self.applyProperties()

    @classmethod
    def getElement(cls, targetId: str):
        for element in cls.SymbolTable:
            if element.id == targetId:
                return element

        return None

    def getErrors(self):

        errors = []

        for lexicError in Lexer.lexicErrors:
            errors.append({
                'type': 'Lexico',
                'row': str(lexicError.row),
                'column': str(lexicError.col),
                'lexema': lexicError.lexeme,
                'expected': "",
                'description': lexicError.msg
            })

        for syntaxError in Parser.syntaxErrors:
            errors.append({
                'type': 'Sintactico',
                'row': str(syntaxError.recivedToken.row),
                'column':  str(syntaxError.recivedToken.col),
                'lexema': syntaxError.recivedToken.lexeme,
                'expected': syntaxError.getExpectedValues(),
                'description': "Valor no esperado"
            })

        return errors

    def createSymbolTable(self):

        # this element is the root of the html tree
        Core.SymbolTable.append(HtmlElement("this", HtmlElementType.BODY))

        # * analyze the controls scope

        index = 0
        while index < len(Lexer.tokenFlow):
            token = Lexer.tokenFlow[index]

            if token.idType == idType.CONTROL:
                nextToken = Lexer.tokenFlow[index + 1]
                element = HtmlElementFactory(token.lexeme, nextToken.lexeme)
                Core.SymbolTable.append(element.createElement())

            index += 1

    def applyProperties(self):

        # Skip definition scope
        index = 0
        while index < len(Lexer.tokenFlow):
            token = Lexer.tokenFlow[index]

            if token.tokenType == TokenType.DEFINITION_SCOPE_CLOSING:
                index += 1
                break
            index += 1

        while index < len(Lexer.tokenFlow):
            tokenFlow = Lexer.tokenFlow

            if tokenFlow[index].idType == idType.VARIABLE:
                targetId = tokenFlow[index].lexeme
                targetAttribute = tokenFlow[index + 2].lexeme
                params = []

                # parameters
                for j in range(index+4, len(tokenFlow)):

                    if tokenFlow[j].tokenType == TokenType.COMMA:
                        continue

                    if tokenFlow[j].tokenType == TokenType.PARENTHESIS_CLOSING:
                        index = j
                        break

                    params.append(tokenFlow[j])

                # Execute function
                function = HtmlFunctionFactory(targetId, targetAttribute, params)
                res = function.applyFunction()
                if res != True:
                    Core.runTimeErrors.append({
                        'type': 'runtime',
                        'row': str(tokenFlow[index].row),
                        'column':  str(tokenFlow[index].col),
                        'lexema': "",
                        'expected': "",
                        'description': res
                    })

            index += 1
