from enum import Enum

TokenType = Enum(
    "TokenType", 
    "COMMA DOT MINUS PLUS SEMICOLON LEFTPARENT RIGHTPARENT LEFTBRACE RIGHTBRACE LESS GREATER",
    "LESSEQUAL GRETEREQUAL EQUAL",
    "AND IF OR PRINT INPUT RETURN TRUE FALSE ELSE",
    "STRING",
    "EOF"
)

class Token:

    def __init__(self, token_type : TokenType, lexeme : str, literal : str, line : int):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self):
        return self.token_type + " " + self.lexeme + " " + self.literal
