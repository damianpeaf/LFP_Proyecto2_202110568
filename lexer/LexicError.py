
class LexicError():
    def __init__(self, lexeme, msg, row, col):
        self.msg = msg
        self.row = row
        self.col = col
        self.lexeme = lexeme

    def __str__(self):
        return "LexicError: %s at row %d, column %d" % (self.msg, self.row, self.col)
