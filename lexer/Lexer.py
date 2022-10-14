from typing import List
from lexer.DFA import DFA

from lexer.Token import Token


class Lexer():

    tokenFlow: List[Token] = []

    def __init__(self, sourceStr: str):
        self.sourceStr = sourceStr
        self.dfa = DFA(self.sourceStr)

    def runLexicAnalysis(self):
        resp = True

        while resp != None:
            resp = self.dfa.getNextToken()

            if resp != None:
                self.tokenFlow.append(resp)

        self.printTokenFlow()
        return self.tokenFlow

    def printTokenFlow(self):
        for token in self.tokenFlow:
            print("TIPO: ", token.tokenType, "  |   LEXEMA: ", token.lexeme)
