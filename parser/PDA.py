
from typing import List
from lexer.Token import Token, TokenType
from parser.NonTerminal import NonTerminal
from constants.validScopeToken import CONTROL_SCOPE_TOKEN, PROPERTIES_SCOPE_TOKEN, LOCATION_SCOPE_TOKEN, OPEN_SCOPE_TOKEN, CLOSE_SCOPE_TOKEN
from constants.validControlToken import VALID_CONTROL_TOKEN
from constants.validVariableToken import VALID_VARIABLE_TOKEN
from constants.validFunctionToken import VALID_FUNCTION_TOKEN
from constants.validUtilToken import OPEN_PARENTHESIS_TOKEN, CLOSE_PARENTHESIS_TOKEN, COMMA_TOKEN, POINT_TOKEN, SEMICOLON_TOKEN, EOF_TOKEN, BOOLEAN_TOKEN, NUMBER_TOKEN, STRING_TOKEN


class PDA():

    def __init__(self, tokenFlow: list):
        self.stack = []
        self.tokenFlow: List[Token] = tokenFlow
        self.currentTokenIndex = 0
        self._init()

    def _init(self):
        self.stack = []
        self._stackPush(EOF_TOKEN)
        self._stackPush(NonTerminal.S)

    def evalTokens(self):
        while self.currentTokenIndex < len(self.tokenFlow):
            pass

    def _evalState(self):
        evaluatedToken = self.tokenFlow[self.currentTokenIndex]

        # * NonTerminal replacement rules
        # ? isinstance(self._stackTop(), NonTerminal)

        # S -> 4 11 A 11 5 4 11 B 11 5 4 11 C 11 5
        if self._stackTop() == NonTerminal.S:

            replace = [
                OPEN_SCOPE_TOKEN,
                CONTROL_SCOPE_TOKEN,
                NonTerminal.A,
                CONTROL_SCOPE_TOKEN,
                CLOSE_SCOPE_TOKEN,
                OPEN_SCOPE_TOKEN,
                PROPERTIES_SCOPE_TOKEN,
                NonTerminal.B,
                PROPERTIES_SCOPE_TOKEN,
                CLOSE_SCOPE_TOKEN,
                OPEN_SCOPE_TOKEN,
                LOCATION_SCOPE_TOKEN,
                NonTerminal.C,
                LOCATION_SCOPE_TOKEN,
                CLOSE_SCOPE_TOKEN,
            ]
            self._replaceTop(replace)
            return True

        # A -> 11 11 7 A | epsilon
        if self._stackTop() == NonTerminal.A:
            # ! Preanalysis
            if evaluatedToken.tokenType == TokenType.ID:
                replace = [
                    VALID_CONTROL_TOKEN,
                    VALID_VARIABLE_TOKEN,
                    SEMICOLON_TOKEN
                ]
                self._replaceTop(replace)
                return True

            # | epsilon
            self._stackPop()
            return True

        # B -> 11 6 11 12 D 13 7 B | epsilon
        if self._stackTop() == NonTerminal.B:
            if evaluatedToken.tokenType == TokenType.ID:
                replace = [
                    VALID_VARIABLE_TOKEN,
                    POINT_TOKEN,
                    VALID_FUNCTION_TOKEN,
                    OPEN_PARENTHESIS_TOKEN,
                    SEMICOLON_TOKEN,
                    NonTerminal.D,
                    CLOSE_PARENTHESIS_TOKEN,
                    SEMICOLON_TOKEN,
                    NonTerminal.B
                ]
                self._replaceTop(replace)
                return True

            # | epsilon
            self._stackPop()
            return True

        # D -> 8 | D -> 9 | D -> 10 | D -> 11
        if self._stackTop() == NonTerminal.D:
            # bool
            if evaluatedToken.tokenType == TokenType.BOOLEAN:
                replace = [
                    BOOLEAN_TOKEN,
                    NonTerminal.E
                ]
                self._replaceTop(replace)
                return True

            # number
            if evaluatedToken.tokenType == TokenType.NUMBER:
                replace = [
                    NUMBER_TOKEN,
                    NonTerminal.E
                ]
                self._replaceTop(replace)
                return True

            # string
            if evaluatedToken.tokenType == TokenType.STRING:
                replace = [
                    STRING_TOKEN,
                    NonTerminal.E
                ]
                self._replaceTop(replace)
                return True

            # VARIABLE
            if evaluatedToken.tokenType == TokenType.ID:
                replace = [
                    VALID_VARIABLE_TOKEN,
                    NonTerminal.E
                ]
                self._replaceTop(replace)
                return True

            # ! error, MISSING PARAMETER
            return False

        # E -> 14 D | epsilon
        if self._stackTop() == NonTerminal.E:
            if evaluatedToken.tokenType == TokenType.COMMA:
                replace = [
                    COMMA_TOKEN,
                    NonTerminal.D
                ]
                self._replaceTop(replace)
                return True

            # | epsilon
            self._stackPop()
            return True

    def _stackTop(self):
        return self.stack[-1]

    def _stackPop(self):
        return self.stack.pop()

    def _stackPush(self, item):
        self.stack.append(item)

    def _replaceTop(self, items):
        self._stackPop()
        for item in items[::-1]:
            self._stackPush(item)
