class AbstractStatement:

    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class ExpressionStatement(AbstractStatement):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        visitor.visit_expression(self)


class PrintStatement(AbstractStatement):

    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        visitor.visit_print(self)


class IfStatement(AbstractStatement):

    def __init__(self, condition, thenbranch, elsebranch):
        self.condition = condition
        self.thenbranch = thenbranch
        self.elsebranch = elsebranch

    def accept(self, visitor):
        visitor.visit_if(self)


class WhileStatement(AbstractStatement):

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def accept(self, visitor):
        visitor.visit_while(self)
