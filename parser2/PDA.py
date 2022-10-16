
from typing import List
from parser2.SyntaxError import SyntaxError
from lexer.Token import Token, TokenType
from parser2.NonTerminal import NonTerminal
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
            resp = self._evalState()

            if isinstance(resp, SyntaxError):
                return resp

        return None

    def _evalState(self):
        evaluatedToken = self.tokenFlow[self.currentTokenIndex]
        stackTop = self._stackTop()

        # * NonTerminal replacement rules
        # ? isinstance(self._stackTop(), NonTerminal)

        # EOF
        if stackTop == EOF_TOKEN:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # S -> 4 11 A 11 5 4 11 B 11 5 4 11 C 11 5
        if stackTop == NonTerminal.S:

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
                NonTerminal.B,
                LOCATION_SCOPE_TOKEN,
                CLOSE_SCOPE_TOKEN,
            ]
            self._replaceTop(replace)
            return True

        # A -> 11 11 7 A | epsilon
        if stackTop == NonTerminal.A:
            # ! Preanalysis
            if evaluatedToken.tokenType == TokenType.ID and evaluatedToken.lexeme not in CONTROL_SCOPE_TOKEN.lexeme and evaluatedToken.lexeme not in PROPERTIES_SCOPE_TOKEN.lexeme and evaluatedToken.lexeme not in LOCATION_SCOPE_TOKEN.lexeme:
                replace = [
                    VALID_CONTROL_TOKEN,
                    VALID_VARIABLE_TOKEN,
                    SEMICOLON_TOKEN,
                    NonTerminal.A
                ]
                self._replaceTop(replace)
                return True

            # | epsilon
            self._stackPop()
            return True

        # B -> 11 6 11 12 D 13 7 B | epsilon
        if stackTop == NonTerminal.B:
            if evaluatedToken.tokenType == TokenType.ID and evaluatedToken.lexeme not in CONTROL_SCOPE_TOKEN.lexeme and evaluatedToken.lexeme not in PROPERTIES_SCOPE_TOKEN.lexeme and evaluatedToken.lexeme not in LOCATION_SCOPE_TOKEN.lexeme:
                replace = [
                    VALID_VARIABLE_TOKEN,
                    POINT_TOKEN,
                    VALID_FUNCTION_TOKEN,
                    OPEN_PARENTHESIS_TOKEN,
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
        if stackTop == NonTerminal.D:
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

            return SyntaxError(evaluatedToken, [BOOLEAN_TOKEN, NUMBER_TOKEN, STRING_TOKEN, VALID_VARIABLE_TOKEN])

        # E -> 14 D | epsilon
        if stackTop == NonTerminal.E:
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

        # * Terminal replacement rules

        # 4 -> <!--
        if stackTop == OPEN_SCOPE_TOKEN and evaluatedToken.tokenType == TokenType.DEFINITION_SCOPE_OPENING:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 5 -> -->
        if stackTop == CLOSE_SCOPE_TOKEN and evaluatedToken.tokenType == TokenType.DEFINITION_SCOPE_CLOSING:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 6 -> .
        if stackTop == POINT_TOKEN and evaluatedToken.tokenType == TokenType.POINT:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 7 -> ;
        if stackTop == SEMICOLON_TOKEN and evaluatedToken.tokenType == TokenType.SEMICOLON:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 8 -> bool
        if stackTop == BOOLEAN_TOKEN and evaluatedToken.tokenType == TokenType.BOOLEAN:
            # Type conversion
            evaluatedToken.lexeme = True if evaluatedToken.lexeme == 'true' else False
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 9 -> number
        if stackTop == NUMBER_TOKEN and evaluatedToken.tokenType == TokenType.NUMBER:
            # Type conversion
            evaluatedToken.lexeme = int(evaluatedToken.lexeme)
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 10 -> string
        if stackTop == STRING_TOKEN and evaluatedToken.tokenType == TokenType.STRING:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 11 -> ID -> VARIABLE | FUNCTION | CONTROL
        if evaluatedToken.tokenType == TokenType.ID and stackTop.tokenType == TokenType.ID:

            if stackTop == VALID_VARIABLE_TOKEN:
                # COPY ID TYPE
                evaluatedToken.idType = VALID_VARIABLE_TOKEN.idType
                self._stackPop()
                self.currentTokenIndex += 1
                return True

            if stackTop == VALID_CONTROL_TOKEN:

                if evaluatedToken.lexeme in VALID_CONTROL_TOKEN.posibleLexemes:
                    # COPY ID TYPE
                    evaluatedToken.idType = VALID_CONTROL_TOKEN.idType
                    self._stackPop()
                    self.currentTokenIndex += 1
                    return True

                return SyntaxError(evaluatedToken, [VALID_CONTROL_TOKEN])

            if stackTop == VALID_FUNCTION_TOKEN:

                if evaluatedToken.lexeme in VALID_FUNCTION_TOKEN.posibleLexemes:
                    # COPY ID TYPE
                    evaluatedToken.idType = VALID_FUNCTION_TOKEN.idType
                    self._stackPop()
                    self.currentTokenIndex += 1
                    return True

                return SyntaxError(evaluatedToken, [VALID_FUNCTION_TOKEN])

            if stackTop == CONTROL_SCOPE_TOKEN:
                # COPY ID TYPE
                evaluatedToken.idType = CONTROL_SCOPE_TOKEN.idType
                self._stackPop()
                self.currentTokenIndex += 1
                return True

            if stackTop == LOCATION_SCOPE_TOKEN:
                # COPY ID TYPE
                evaluatedToken.idType = LOCATION_SCOPE_TOKEN.idType
                self._stackPop()
                self.currentTokenIndex += 1
                return True

            if stackTop == PROPERTIES_SCOPE_TOKEN:
                # COPY ID TYPE
                evaluatedToken.idType = PROPERTIES_SCOPE_TOKEN.idType
                self._stackPop()
                self.currentTokenIndex += 1
                return True

        # 12 -> (
        if stackTop == OPEN_PARENTHESIS_TOKEN and evaluatedToken.tokenType == TokenType.PARENTHESIS_OPENING:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 13 -> )
        if stackTop == CLOSE_PARENTHESIS_TOKEN and evaluatedToken.tokenType == TokenType.PARENTHESIS_CLOSING:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        # 14 -> ,
        if stackTop == COMMA_TOKEN and evaluatedToken.tokenType == TokenType.COMMA:
            self._stackPop()
            self.currentTokenIndex += 1
            return True

        print('SyntaxError: Unexpected token', self.currentTokenIndex)
        return SyntaxError(evaluatedToken, [stackTop])

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
