from lexer.Lexer import Lexer
from parser2.PDA import PDA
from parser2.SyntaxError import SyntaxError


class Parser():

    def __init__(self):
        pass

    def runSyntacticAnalysis(self):

        if len(Lexer.lexicErrors) > 0:
            print("Lexic errors found, aborting sintax analysis")
            raise Exception("Lexic errors found, aborting sintax analysis")

        if len(Lexer.tokenFlow) == 0:
            print("No tokens found, aborting sintax analysis")
            raise Exception("No tokens found, aborting sintax analysis")

        resp = True
        pda = PDA(Lexer.tokenFlow)
        while resp == True:
            resp = pda.evalTokens()

        if isinstance(resp, SyntaxError):
            print(resp)

        print("Sintax analysis completed successfully")
