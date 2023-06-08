from tokens import Token, TokenType, string_to_token


class Tokenizer:

    def __init__(self, src: str):
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.src = src

    def to_tokens(self) -> list:
        while not self.at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def at_end(self) -> bool:
        return self.current >= len(self.src)

    def scan_token(self):
        # TODO: scan for tokens

        c = self.advance()

        # simply skipping all kind of spaces
        if c == ' ' or c == '\t' or c == '\r':
            return

        # newline
        if c == '\n':
            self.line += 1
            self.add_token(TokenType.NEWLINE)
            return

        # reading comments
        if c == '\'':
            while self.peek() != '\n':
                self.advance()
            return

        if c == '(':
            self.add_token(TokenType.LEFTPARENT)
            return
        if c == ')':
            self.add_token(TokenType.RIGHTPARENT)
            return
        if c == '{':
            self.add_token(TokenType.LEFTCURLY)
            return
        if c == '}':
            self.add_token(TokenType.RIGHTCURLY)
            return
        if c == '[':
            self.add_token(TokenType.LEFTSQUARE)
            return
        if c == ']':
            self.add_token(TokenType.RIGHTSQUARE)
            return
        if c == '*':
            self.add_token(TokenType.STAR)
            return
        if c == '+':
            self.add_token(TokenType.PLUS)
            return
        if c == '-':
            self.add_token(TokenType.MINUS)
            return
        if c == ';':
            self.add_token(TokenType.SEMICOLON)
            return
        if c == '.':
            self.add_token(TokenType.DOT)
            return
        if c == ',':
            self.add_token(TokenType.COMMA)
            return
        if c == '/':
            self.add_token(TokenType.SLASH)
            return
        if c == '!':
            self.add_token(TokenType.NOTEQUAL if self.conditional_advance('=') else TokenType.NOT)  # nopep8
            return
        if c == '=':
            self.add_token(TokenType.EQUALEQUAL if self.conditional_advance('=') else TokenType.EQUAL)  # nopep8
            return
        if c == '<':
            self.add_token(TokenType.LESSEQUAL if self.conditional_advance('=') else TokenType.LESS)  # nopep8
            return
        if c == '>':
            self.add_token(TokenType.GREATEREQUAL if self.conditional_advance('=') else TokenType.GREATER)  # nopep8
            return

        # reading string
        if c == '\"':
            self.read_string()
            return

        if self.is_digit(c):
            self.read_number()
            return

        if self.is_alpha(c):
            self.read_keyword()
            return

        raise SyntaxError(f"Syntax Error in line {self.line}")

    def add_token(self, tkn: TokenType, literal=None) -> None:
        text = self.src[self.start: self.current]
        self.tokens.append(Token(tkn, text, literal, self.line))

    def advance(self) -> str:
        self.current += 1
        return self.src[self.current - 1]

    def conditional_advance(self, expected: str) -> bool:
        if self.at_end():
            return False
        if self.src[self.current] != expected:
            return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.at_end():
            return '\0'
        return self.src[self.current]

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.src):
            return '\0'
        return self.src[self.current + 1]

    def read_string(self) -> None:
        while not self.at_end() and self.peek() != '\"':
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.at_end():
            raise SyntaxError("No matching \"")

        self.advance()

        self.add_token(TokenType.STRING,
                       self.src[self.start + 1: self.current - 1])

    def is_digit(self, c: str) -> bool:
        return '0' <= c and c <= '9'

    def read_number(self) -> None:
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.src[self.start: self.current]))  # nopep8

    def is_alpha(self, c: str) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

    def is_alpha_or_digit(self, c: str) -> bool:
        return self.is_alpha(c) or self.is_digit(c) or c == '_'

    def read_keyword(self):
        while self.is_alpha_or_digit(self.peek()):
            self.advance()
        kwrd = self.src[self.start: self.current]
        kwrd = kwrd.lower()
        result = TokenType.IDENTIFIER
        if kwrd in string_to_token:
            result = string_to_token[kwrd]
            self.add_token(result)
        else:
            self.add_token(result, kwrd)
