from tokentypes.tokens import TokenType


class Visitor:
    def __init__(self):
        pass

    def visit_binary(self, expr):
        pass

    def visit_unary(self, expr):
        pass

    def visit_grouping(self, expr):
        pass

    def visit_literal(self, expr):
        pass


class Executor(Visitor):

    def __init__(self):
        pass

    def visit_binary(self, expr):

        # TODO: type checking

        left = expr.left
        right = expr.right

        if expr.operator.token_type == TokenType.MINUS:
            return left - right

        if expr.operator.token_type == TokenType.SLASH:
            return left / right

        if expr.operator.token_type == TokenType.STAR:
            return left * right

        if expr.operator.token_type == TokenType.GREATER:
            return left > right
        if expr.operator.token_type == TokenType.GREATEREQUAL:
            return left >= right
        if expr.operator.token_type == TokenType.LESS:
            return left < right
        if expr.operator.token_type == TokenType.LESSEQUAL:
            return left <= right

        if expr.operator.token_type == TokenType.NOTEQUAL:
            return left != right

        if expr.operator.token_type == TokenType.EQUALEQUAL:
            return left == right

        return None

    def visit_unary(self, expr):
        right = expr.right

        if expr.operator.token_type == TokenType.MINUS:
            return -right

        if expr.operator.token_type == TokenType.NOT:
            return not self.is_truth(right)

        return None

    def visit_grouping(self, expr):
        return self.evaluate(expr.expr)

    def visit_literal(self, expr):
        return expr.value

    def evaluate(self, expr):
        return expr.accept(self)

    def is_truth(self, obj):
        return bool(obj)
