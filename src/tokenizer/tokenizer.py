from tokens import Token, TokenType
class Tokenizer:

    def __init__(self, src : str):
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.src = src

    def to_tokens(self):
        while not self.at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
    
    def at_end(self) -> bool:
        """
        Check, if the file has ended

        Returns:
            bool: True if file has ended, False otherwise
        """
        return self.current > len(self.src)

    def scan_token(self):
        """_summary_

        Raises:
            SyntaxError: _description_
        """
        # TODO: scan for tokens

        c = self.advance()

        if c == ' ' or c == '\t' or c == '\r':
            return
        
        if c == '\n':
            self.line += 1
            return

        raise SyntaxError(f"Syntax Error in line {self.line}") 

    def add_token(self, tkn : TokenType, literal = None):
        text = self.src[self.start : self.current]
        self.tokens.append(Token(tkn, text, literal, self.line))

    def advance(self) -> chr:
        """
        Get char and increase self.current

        Returns:
            chr: char on self.current
        """
        self.current += 1
        return self.src[self.current - 1]
    
    def conditional_advance(self, expected : chr) -> bool:
        if self.at_end():
            return False
        if self.src[self.current] != expected:
            return False
        self.current += 1
        return True

    def peek(self):
        if self.at_end():
            return '\0'
        return self.src[self.current]
    
    def read_string(self):
        while not self.at_end() and self.peek() != '\"':
            if self.peen() == '\n':
                self.line += 1
            self.advance()
        
        if self.at_end():
            raise SyntaxError("No matching \"")
        
        self.advance()

        self.add_token(TokenType.STRING, self.src[self.start + 1, self.current - 1])

    def is_digit(self, c : str):
        if '0' <= c and c <= '9':
            return True
        return False        