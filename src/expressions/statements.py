class AbstractStatement:

    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class Expression(AbstractStatement):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        visitor.visit_expression(self)


class PrintStatement(AbstractStatement):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        visitor.visit_print(self)
