from constants.idType import idType
from lexer.Token import Token, TokenType


t1 = Token(TokenType.ID, "Controles")
t1.idType = idType.SCOPE
CONTROL_SCOPE_TOKEN = t1


t2 = Token(TokenType.ID, "propiedades")
t2.idType = idType.SCOPE
PROPERTIES_SCOPE_TOKEN = t2

t3 = Token(TokenType.ID, "Colocacion")
t3.idType = idType.SCOPE
LOCATION_SCOPE_TOKEN = t3

OPEN_SCOPE_TOKEN = Token(TokenType.DEFINITION_SCOPE_OPENING, "<!--")
CLOSE_SCOPE_TOKEN = Token(TokenType.DEFINITION_SCOPE_CLOSING, "-->")
