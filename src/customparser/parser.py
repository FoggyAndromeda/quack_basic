from tokenizer.tokenizer import TokenType, Token
from expressions.expressions import *


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            return self.expression()
        except:
            return

    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparsion()

        while self.match(TokenType.EQUALEQUAL, TokenType.NOTEQUAL):
            operator = self.previous()
            right = self.comparsion()
            expr = Binary(expr, operator, right)

        return expr

    def comparsion(self):
        expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GRETEREQUAL, TokenType.LESS, TokenType.LESSEQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()

        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self):
        if self.match(TokenType.NOT, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(False)
        if self.match(TokenType.NULL):
            return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.LEFTPARENT):
            expr = self.expression()
            self.consume(TokenType.RIGHTPARENT, "Expected \')\'")
            return Grouping(expr)

    def match(self, *types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, type):
        if self.at_end():
            return False
        return self.peek().type == type

    def advance(self):
        if not self.at_end():
            self.current += 1
        return self.previous()

    def at_end(self):
        return self.peek().type == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def consume(self, type, message):
        if self.check(type):
            return self.advance()

        raise RuntimeError(message)

    def synchronize(self):
        self.advance()

        while not self.at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return

            if self.peek().type == TokenType.FOR:
                pass
            if self.peek().type == TokenType.WHILE:
                pass
            if self.peek().type == TokenType.IF:
                pass
            if self.peek().type == TokenType.PRINT:
                pass
            if self.peek().type == TokenType.RETURN:
                return

            self.advance()
