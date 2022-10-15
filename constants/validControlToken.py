

from constants.idType import idType
from lexer.Token import Token, TokenType


VALID_CONTROL_TOKENS_LEXEMES = [
    "Etiqueta",
    "Boton",
    "Check",
    "RadioBoton",
    "Texto",
    "AreaTexto",
    "Clave",
    "Contenedor",
]

token = Token(TokenType.ID)
token.posibleLexemes = VALID_CONTROL_TOKENS_LEXEMES
token.idType = idType.CONTROL


VALID_CONTROL_TOKEN = token
