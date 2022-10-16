from lexer.Lexer import Lexer
from parser2.Parser import Parser


class Core():

    def __init__(self):
        pass

    def getErrors(self):

        errors = []

        for lexicError in Lexer.lexicErrors:
            errors.append({
                'type': 'Lexico',
                'row': str(lexicError.row),
                'column': str(lexicError.col),
                'lexema': lexicError.lexeme,
                'expected': "",
                'description': lexicError.msg
            })

        for syntaxError in Parser.syntaxErrors:
            errors.append({
                'type': 'Sintactico',
                'row': str(syntaxError.recivedToken.row),
                'column':  str(syntaxError.recivedToken.col),
                'lexema': syntaxError.recivedToken.lexeme,
                'expected': syntaxError.getExpectedValues(),
                'description': "Valor no esperado"
            })

        return errors
