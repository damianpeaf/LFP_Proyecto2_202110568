from lexer.Lexer import Lexer


class Parser():

    def __init__(self):
        pass

    def runSintaxAnalysis(self):

        if len(Lexer.lexicErrors) > 0:
            print("Lexic errors found, aborting sintax analysis")
            raise Exception("Lexic errors found, aborting sintax analysis")

        if len(Lexer.tokenFlow) == 0:
            print("No tokens found, aborting sintax analysis")
            raise Exception("No tokens found, aborting sintax analysis")

        print("Sintax analysis completed successfully")
