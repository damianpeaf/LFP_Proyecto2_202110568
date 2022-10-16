from constants.letter import LETTERS
from constants.numbers import NUMBERS
from lexer.LexicError import LexicError
from lexer.Token import Token, TokenType


class DFA():

    def __init__(self, stringFlow: str):
        self.state = 0
        self.lexeme = ""
        self.stringFlow = stringFlow.strip()

        self.currentIndex = 0
        self.row = 1
        self.col = 1

        self.skipBlankSpaces = True
        self.skipLineBreaks = True
        self.skipLine = False
        self.skipToken = False

    def getNextToken(self):

        while self.currentIndex < len(self.stringFlow):
            token = None
            currentCharacter = self.stringFlow[self.currentIndex]

            # Comments

            # * Skips line
            if self.skipLine:
                self.currentIndex += 1
                self.col += 1

                if currentCharacter == '\n':
                    self.row += 1
                    self.col = 1
                    self.skipLine = False

                continue

            # * Skips line breaks
            if self.skipLineBreaks and currentCharacter == '\n':
                token = self._evalAcceptanceState()
                self.row += 1
                self.col = 1
                self.currentIndex += 1

            if token == None:
                token = self._evalCharacter()

            if token == True:
                self.col += 1
                self.currentIndex += 1
                continue
            if isinstance(token, Token):

                if token.tokenType == TokenType.ONELINE_COMMENT_OPENING:
                    self.skipLine = True
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                if token.tokenType == TokenType.MULTILINE_COMMENT_OPENING:
                    self.skipToken = True
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                if token.tokenType == TokenType.MULTILINE_COMMENT_CLOSING:
                    self.skipToken = False
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                if self.skipToken:
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                return token

            if isinstance(token, LexicError):
                return token

        if self.lexeme != '':
            return self._evalAcceptanceState()

        return None

    # True -> valid state/character
    # False -> invalid state/character
    # Token -> valid token/lexeme
    # LexicError -> invalid token/lexeme
    def _evalCharacter(self):
        currentCharacter = self.stringFlow[self.currentIndex]

        if currentCharacter == ' ':

            if self.skipBlankSpaces:
                token = self._evalAcceptanceState()
                self.col += 1
                self.currentIndex += 1
                return token
            else:
                self.lexeme += currentCharacter
                return True

        if self.state == 0:
            if currentCharacter == '/':
                self.state = 1
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "*":
                self.state = 4
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "<":
                self.state = 6
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ".":
                self.state = 11
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ";":
                self.state = 12
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ",":
                self.state = 13
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "(":
                self.state = 14
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ")":
                self.state = 15
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "t":
                self.state = 16
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "f":
                self.state = 20
                self.lexeme += currentCharacter
                return True
            if currentCharacter in NUMBERS:
                self.state = 24
                self.lexeme += currentCharacter
                return True
            if currentCharacter == '\"':
                self.skipBlankSpaces = False
                self.state = 25
                self.lexeme += currentCharacter
                return True
            if currentCharacter in LETTERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True
            if currentCharacter == '-':
                self.state = 29
                self.lexeme += currentCharacter
                return True

        if self.state == 1:
            if currentCharacter == '/':
                self.state = 2
                self.lexeme += currentCharacter
                return True

            if currentCharacter == '*':
                self.state = 3
                self.lexeme += currentCharacter
                return True

        if self.state == 4:
            if currentCharacter == '/':
                self.state = 5
                self.lexeme += currentCharacter
                return True

        if self.state == 6:
            if currentCharacter == "!":
                self.state = 7
                self.lexeme += currentCharacter
                return True

        if self.state == 7:
            if currentCharacter == "-":
                self.state = 8
                self.lexeme += currentCharacter
                return True

        if self.state == 8:
            if currentCharacter == "-":
                self.state = 9
                self.lexeme += currentCharacter
                return True

        if self.state == 16:
            if currentCharacter == "r":
                self.state = 17
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 17:
            if currentCharacter == "u":
                self.state = 18
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 18:
            if currentCharacter == "e":
                self.state = 19
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 20:
            if currentCharacter == "a":
                self.state = 21
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 21:
            if currentCharacter == "l":
                self.state = 22
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 22:
            if currentCharacter == "s":
                self.state = 23
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 23:
            if currentCharacter == "e":
                self.state = 19
                self.lexeme += currentCharacter
                return True

            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 24:
            if currentCharacter in NUMBERS:
                self.state = 24
                self.lexeme += currentCharacter
                return True

        if self.state == 25:
            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 26
                self.lexeme += currentCharacter
                return True

            if currentCharacter == '\"':
                self.state = 27
                self.lexeme += currentCharacter
                return True

        if self.state == 26:
            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 26
                self.lexeme += currentCharacter
                return True

            if currentCharacter == '\"':
                self.state = 27
                self.lexeme += currentCharacter
                return True

        if self.state == 28:
            if currentCharacter in LETTERS or currentCharacter in NUMBERS:
                self.state = 28
                self.lexeme += currentCharacter
                return True

        if self.state == 29:
            if currentCharacter == '-':
                self.state = 30
                self.lexeme += currentCharacter
                return True

        if self.state == 30:
            if currentCharacter == ">":
                self.state = 31
                self.lexeme += currentCharacter
                return True

        return self._evalAcceptanceState()

    def _resetAutomaton(self):
        self.state = 0
        self.lexeme = ""

    def _evalAcceptanceState(self):

        if self.state == 0:
            self.currentIndex -= 1
            return True

        if self.state == 2:
            token = self._generateToken(TokenType.ONELINE_COMMENT_OPENING)
            self._resetAutomaton()
            return token
        if self.state == 3:
            token = self._generateToken(TokenType.MULTILINE_COMMENT_OPENING)
            self._resetAutomaton()
            return token
        if self.state == 5:
            token = self._generateToken(TokenType.MULTILINE_COMMENT_CLOSING)
            self._resetAutomaton()
            return token
        if self.state == 9:
            token = self._generateToken(TokenType.DEFINITION_SCOPE_OPENING)
            self._resetAutomaton()
            return token
        if self.state == 11:
            token = self._generateToken(TokenType.POINT)
            self._resetAutomaton()
            return token
        if self.state == 12:
            token = self._generateToken(TokenType.SEMICOLON)
            self._resetAutomaton()
            return token
        if self.state == 13:
            token = self._generateToken(TokenType.COMMA)
            self._resetAutomaton()
            return token
        if self.state == 14:
            token = self._generateToken(TokenType.PARENTHESIS_OPENING)
            self._resetAutomaton()
            return token
        if self.state == 15:
            token = self._generateToken(TokenType.PARENTHESIS_CLOSING)
            self._resetAutomaton()
            return token
        if self.state == 16 or self.state == 17 or self.state == 18 or self.state == 20 or self.state == 21 or self.state == 22 or self.state == 23:
            token = self._generateToken(TokenType.ID)
            self._resetAutomaton()
            return token
        if self.state == 19:
            token = self._generateToken(TokenType.BOOLEAN)
            self._resetAutomaton()
            return token
        if self.state == 24:
            token = self._generateToken(TokenType.NUMBER)
            self._resetAutomaton()
            return token
        if self.state == 27:
            self.lexeme = self.lexeme.replace("\"", "")
            token = self._generateToken(TokenType.STRING)
            self.skipBlankSpaces = True
            self._resetAutomaton()
            return token
        if self.state == 28:
            token = self._generateToken(TokenType.ID)
            self._resetAutomaton()
            return token
        if self.state == 31:
            token = self._generateToken(TokenType.DEFINITION_SCOPE_CLOSING)
            self._resetAutomaton()
            return token

        error = self._generateError("Invalid token")
        self._resetAutomaton()
        return error

    def _generateToken(self, tokenType):
        token = Token(tokenType, self.lexeme, self.row, self.col)
        return token

    def _generateError(self, msg) -> LexicError:
        return LexicError(self.lexeme, msg, self.row, self.col)
