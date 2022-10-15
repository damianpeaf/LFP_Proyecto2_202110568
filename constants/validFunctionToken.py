

from constants.idType import idType
from lexer.Token import Token, TokenType


VALID_FUNCTION_TOKENS_LEXEMES = [
    "setColorLetra",
    "setTexto",
    "setAlineacion",
    "setColorFondo",
    "setMarcada",
    "setGrupo",
    "setAncho",
    "setAlto",
    "setPosicion",
    "add",
]

token = Token(TokenType.ID)
token.posibleLexemes = VALID_FUNCTION_TOKENS_LEXEMES
token.idType = idType.FUNCTION


VALID_FUNCTION_TOKEN = token
