from src.tokentypes.tokens import TokenType
from src.environment.environment import Environment


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

    def visit_assignment(self, expr):
        pass

    def visit_variable(self, expr):
        pass


class Executor(Visitor):

    def __init__(self):
        self.env = Environment()
        self.output_buffer = []

    def interpret(self, expr):
        try:
            value = self.evaluate(expr)
            return value
        except Exception as e:
            print(f"Error in Executor: {e}")

    def evaluate(self, expr):
        if not expr is None:
            return expr.accept(self)

    def visit_binary(self, expr):

        # TODO: type checking

        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.token_type == TokenType.PLUS:
            return left + right

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
        right = self.evaluate(expr.right)

        if expr.operator.token_type == TokenType.MINUS:
            return -right

        if expr.operator.token_type == TokenType.NOT:
            return not self.is_truth(right)

        return None

    def visit_grouping(self, expr):
        return self.evaluate(expr.expr)

    def visit_literal(self, expr):
        return expr.value

    def is_truth(self, obj):
        return bool(self.evaluate(obj))

    def visit_assignment(self, expr):
        if self.env.check_variable_existance(expr.name):
            self.env.create_variable(expr.name, expr.value)
        else:
            self.env.change_variable(expr.name, expr.value)
        return self.env.get_variable(expr.name)

    def visit_variable(self, expr):
        var_name = expr.name.lexeme
        if self.env.check_variable_existance(var_name):
            return self.env.get_variable(var_name)

    def visit_print(self, statement):
        value = self.evaluate(statement.expr)
        self.output_buffer.append(str(value))
        return None

    def visit_expression(self, statement):
        self.evaluate(statement.expr)
        return None

    def visit_assignation(self, expr):
        variable_name = expr.name.lexeme
        value = self.evaluate(expr.value)
        if self.env.check_variable_existance(variable_name):
            self.env.change_variable(variable_name, value)
        else:
            self.env.create_variable(variable_name, value)

    def visit_if(self, statement):
        if self.is_truth(statement.condition):
            self.evaluate(statement.thenbranch)
        elif not statement.elsebranch is None:
            self.evaluate(statement.elsebranch)

    def visit_while(self, statement):
        while self.is_truth(statement.condition):
            for stmnt in statement.body:
                self.evaluate(stmnt)

    def get_buffer(self):
        return self.output_buffer