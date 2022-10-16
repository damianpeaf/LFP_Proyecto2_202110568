from typing import List
from lexer.Lexer import Lexer
from parser2.PDA import PDA
from parser2.SyntaxError import SyntaxError


class Parser():

    syntaxErrors: List[SyntaxError] = []

    def __init__(self):
        Parser.syntaxErrors = []

    def runSyntacticAnalysis(self):

        # if len(Lexer.lexicErrors) > 0:
        #     return

        # if len(Lexer.tokenFlow) == 0:
        #     return

        resp = True
        pda = PDA(Lexer.tokenFlow)
        while resp == True:
            resp = pda.evalTokens()

        if isinstance(resp, SyntaxError):
            Parser.syntaxErrors.append(resp)
            return

        return True
