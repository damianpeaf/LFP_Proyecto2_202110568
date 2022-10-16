

from typing import List
from lexer.Token import Token


class SyntaxError():

    def __init__(self,  recivedToken: Token, expectedTokens: List[Token]):
        self.recivedToken = recivedToken
        self.expectedToken = expectedTokens

    def __str__(self):
        expeted = ""

        for token in self.expectedToken:
            expeted += token.tokenType.name + " "

        return f"Syntax error: {self.recivedToken.lexeme} found, expected {expeted}"
