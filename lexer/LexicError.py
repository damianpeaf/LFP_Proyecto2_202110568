
class LexicError():
    def __init__(self, lexeme, msg, line, col):
        self.msg = msg
        self.line = line
        self.col = col
        self.lexeme = lexeme

    def __str__(self):
        return "LexicError: %s at line %d, column %d" % (self.msg, self.line, self.col)
