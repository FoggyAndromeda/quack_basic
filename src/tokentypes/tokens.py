from enum import Enum

TokenType = Enum(
    "TokenType",
    "COMMA DOT MINUS PLUS STAR SLASH SEMICOLON LEFTPARENT RIGHTPARENT LEFTCURLY RIGHTCURLY LEFTSQUARE RIGHTSQUARE LESS GREATER EQUAL NOT \
    LESSEQUAL GREATEREQUAL EQUALEQUAL NOTEQUAL \
    AND IF OR PRINT INPUT RETURN TRUE FALSE ELSE \
    STRING NUMBER\
    IDENTIFIER\
    FOR WHILE FUNCTION NEXT CONST CALL\
    NEWLINE\
    NULL\
    EOF"
)
# TODO: write more tokens (list: https://www.qbasic.net/en/reference/qb11/overview.htm)

# TODO: I belive, that I absolutely shouldn't do this but for now it's ok. I'll replace it later
string_to_token = {
    "for": TokenType.FOR,
    "while": TokenType.WHILE,
    "return": TokenType.RETURN,
    "print": TokenType.PRINT,
    "function": TokenType.FUNCTION,
    "next": TokenType.NEXT,
    "const": TokenType.CONST,
    "call": TokenType.CALL
}


# TODO: should have it's own file
class Token:

    def __init__(self, token_type: TokenType, lexeme: str, literal: str, line: int):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        if (self.lexeme == None):
            return self.token_type.name
        if (self.literal == None):
            return self.token_type.name
        return self.token_type.name + " " + str(self.lexeme) + " " + str(self.literal)
