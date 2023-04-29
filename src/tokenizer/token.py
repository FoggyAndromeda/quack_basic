from enum import Enum

TokenTypes = Enum(
    "Token", 
    "COMMA DOT MINUS PLUS SEMICOLON LEFTPARENT RIGHTPARENT LEFTBRACE RIGHTBRACE LESS GREATER",
    "LESSEQUAL GRETEREQUAL EQUAL",
    "AND IF OR PRINT INPUT RETURN TRUE FALSE ELSE"
)

class Token:

    def __init__(self):
        pass
