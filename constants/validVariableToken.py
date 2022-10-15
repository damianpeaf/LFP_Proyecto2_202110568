from constants.idType import idType
from lexer.Token import Token, TokenType


token = Token(TokenType.ID)
token.idType = idType.VARIABLE
VALID_VARIABLE_TOKEN = token
