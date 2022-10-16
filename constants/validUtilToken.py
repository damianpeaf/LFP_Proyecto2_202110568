from lexer.Token import Token, TokenType


SEMICOLON_TOKEN = Token(TokenType.SEMICOLON, ";")
POINT_TOKEN = Token(TokenType.POINT, ".")
COMMA_TOKEN = Token(TokenType.COMMA, ",")
OPEN_PARENTHESIS_TOKEN = Token(TokenType.PARENTHESIS_OPENING, "(")
CLOSE_PARENTHESIS_TOKEN = Token(TokenType.PARENTHESIS_CLOSING, ")")
BOOLEAN_TOKEN = Token(TokenType.BOOLEAN, "true/false")
NUMBER_TOKEN = Token(TokenType.NUMBER, "Numero")
STRING_TOKEN = Token(TokenType.STRING, "String")
EOF_TOKEN = Token(TokenType.EOF)
EMPTY_TOKEN = Token(TokenType.EMPTY, "")
