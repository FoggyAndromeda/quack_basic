from tokentypes.tokens import Token


class AbstractExpression:

    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class Binary(AbstractExpression):

    def __init__(self,  left: AbstractExpression, operator: Token, right: AbstractExpression):
        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_binary(self)


class Unary(AbstractExpression):

    def __init__(self, operator: Token, right: AbstractExpression):
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_unary(self)


class Grouping(AbstractExpression):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visit_grouping(self)


class Literal(AbstractExpression):

    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_literal(self)
