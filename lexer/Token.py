from enum import Enum, auto


class TokenType(Enum):
    ONELINE_COMMENT_OPENING = auto()
    MULTILINE_COMMENT_OPENING = auto()
    MULTILINE_COMMENT_CLOSING = auto()
    DEFINITION_SCOPE_OPENING = auto()
    DEFINITION_SCOPE_CLOSING = auto()
    POINT = auto()
    SEMICOLON = auto()
    BOOLEAN = auto()
    NUMBER = auto()
    STRING = auto()
    ID = auto()
    PARENTHESIS_OPENING = auto()
    PARENTHESIS_CLOSING = auto()
    COMMA = auto()


class Token():

    def __init__(self, tokenType: TokenType, lexeme: str, row: int, col: int) -> None:
        self.tokenType = tokenType
        self.lexeme = lexeme
        self.row = row
        self.col = col
