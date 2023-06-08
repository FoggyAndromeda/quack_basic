from src.tokenizer.tokenizer import TokenType, Token
from src.expressions.expressions import *
from src.expressions.statements import *


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            statements = []
            while not self.at_end():
                statements.append(self.statement())
            return statements
        except Exception as e:
            print(f"Error in Parser: {e}")
            return

    def statement(self):
        if self.match(TokenType.PRINT):
            return self.print_statement()
        if self.match(TokenType.IF):
            return self.if_statement()
        if self.match(TokenType.WHILE):
            return self.while_statement()
        return self.expression_statement()

    def print_statement(self):
        value = self.expression()
        self.consume(TokenType.NEWLINE, "Expected new line after value")
        return PrintStatement(value)

    def if_statement(self):
        self.consume(TokenType.LEFTPARENT, "Expected ( after IF")
        condition = self.expression()
        self.consume(TokenType.RIGHTPARENT, "Expected ) after condition")

        while self.peek().token_type == TokenType.NEWLINE:
            self.advance()

        self.consume(TokenType.THEN, "Expected THEN after IF")
        thenbranch = self.statement()
        elsebranch = None

        while self.peek().token_type == TokenType.NEWLINE:
            self.advance()

        if self.match(TokenType.ELSE):
            elsebranch = self.statement()
        return IfStatement(condition, thenbranch, elsebranch)

    def while_statement(self):
        self.consume(TokenType.LEFTPARENT, "Expected ( after IF")
        condition = self.expression()
        self.consume(TokenType.RIGHTPARENT, "Expected ) after condition")

        body = []
        while not self.at_end() and self.peek().token_type != TokenType.WEND:
            body.append(self.statement())

        self.consume(TokenType.WEND, "Expected WEND after WHILE statement")
        return WhileStatement(condition, body)

    def expression_statement(self):
        value = self.expression()
        self.consume(TokenType.NEWLINE, "Expected new line after expression")
        return Expression(value)

    def expression(self):
        return self.assignment()

    def assignment(self):
        expr = self.equality()

        if self.match(TokenType.EQUAL):
            var = self.previous()
            value = self.assignment()

            if isinstance(expr, Variable):
                return Assign(expr.name, value)

            raise (f"Wrong target for assignment: {var}")

        return expr

    def equality(self):
        expr = self.comparsion()

        while self.match(TokenType.EQUALEQUAL, TokenType.NOTEQUAL):
            operator = self.previous()
            right = self.comparsion()
            expr = Binary(expr, operator, right)

        return expr

    def comparsion(self):

        expr = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATEREQUAL, TokenType.LESS, TokenType.LESSEQUAL):
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

        if self.match(TokenType.IDENTIFIER):
            return Variable(self.previous())

    def match(self, *types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, type):
        if self.at_end():
            return False
        return self.peek().token_type == type

    def advance(self):
        if not self.at_end():
            self.current += 1
        return self.previous()

    def at_end(self):
        return self.peek().token_type == TokenType.EOF

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
            if self.previous().token_type == TokenType.SEMICOLON:
                return

            if self.peek().token_type == TokenType.FOR:
                pass
            if self.peek().token_type == TokenType.WHILE:
                pass
            if self.peek().token_type == TokenType.IF:
                pass
            if self.peek().token_type == TokenType.PRINT:
                pass
            if self.peek().token_type == TokenType.RETURN:
                return

            self.advance()
