from typing import List
from lexer.DFA import DFA
from lexer.LexicError import LexicError

from lexer.Token import Token


class Lexer():

    tokenFlow: List[Token] = []
    lexicErrors: List[LexicError] = []

    def __init__(self, sourceStr: str):
        self.sourceStr = sourceStr
        self.dfa = DFA(self.sourceStr)
        Lexer.tokenFlow = []
        Lexer.lexicErrors = []

    def runLexicAnalysis(self):
        resp = True

        while resp != None:
            resp = self.dfa.getNextToken()

            if isinstance(resp, Token):
                self.tokenFlow.append(resp)

            elif isinstance(resp, LexicError):
                self.lexicErrors.append(resp)

        # self.printTokenFlow()
        return self.getTokens()

    def getTokens(self):
        tokens = []
        number = 1
        for token in Lexer.tokenFlow:
            tokens.append({'number': number, 'row': token.row, 'column': token.col, 'lexema': token.lexeme, 'type': token.tokenType.name})
            number += 1
        return tokens

    def printTokenFlow(self):
        i = 1
        for token in self.tokenFlow:
            print(str(i), "TIPO: ", token.tokenType, "  |   LEXEMA: ", token.lexeme, "  |   FILA: ", token.row, "  |   COLUMNA: ", token.col)
            i += 1
