

from typing import List
from constants.idType import idType
from lexer.Token import Token, TokenType


class SyntaxError():

    def __init__(self,  recivedToken: Token, expectedTokens: List[Token]):
        self.recivedToken = recivedToken
        self.expectedToken = expectedTokens

    def getExpectedValues(self):

        if len(self.expectedToken) == 1:
            expected = self.expectedToken[0]

            if expected.posibleLexemes != None:
                return "Valores válidos: " + ", ".join(expected.posibleLexemes)

            if expected.lexeme == None:
                return expected.tokenType.name

            return expected.lexeme

        expected = ""
        for token in self.expectedToken:

            if token.idType == idType.VARIABLE:
                expected += "Variable "

            if token.lexeme == None:
                continue
            expected += token.lexeme + " "
        return expected

    def getMsg(self):
        pass

    def __str__(self):
        expected = ""

        for token in self.expectedToken:
            expected += token.tokenType.name + " "

        return f"Syntax error: {self.recivedToken.lexeme} found, expected {expected}"
