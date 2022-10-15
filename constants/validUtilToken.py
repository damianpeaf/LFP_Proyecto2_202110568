from ctypes.wintypes import BOOLEAN
from lexer.Token import Token, TokenType


SEMICOLON_TOKEN = Token(TokenType.SEMICOLON)
POINT_TOKEN = Token(TokenType.POINT)
COMMA_TOKEN = Token(TokenType.COMMA)
OPEN_PARENTHESIS_TOKEN = Token(TokenType.OPEN_PARENTHESIS)
CLOSE_PARENTHESIS_TOKEN = Token(TokenType.CLOSE_PARENTHESIS)
BOOLEAN_TOKEN = Token(TokenType.BOOLEAN)
NUMBER_TOKEN = Token(TokenType.NUMBER)
STRING_TOKEN = Token(TokenType.STRING)
EOF_TOKEN = Token(TokenType.EOF)
