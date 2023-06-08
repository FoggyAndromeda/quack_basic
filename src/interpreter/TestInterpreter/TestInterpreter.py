import unittest
import src.tokenizer.tokenizer as tokenizer
import src.customparser.parser as parser
from src.expressions.visitor import Executor
from src.interpreter.interpreter import Interpreter

# TODO: rewrite as this test fails
class TestInterpreter(unittest.TestCase):
    def test_run_addition(self):
        interp = Interpreter()
        src = """
        a = 10
        b = 20
        PRINT a + b
        """
        tkn = tokenizer.Tokenizer(src)
        tokens = tkn.to_tokens()
        prs = parser.Parser(tokens)
        expression = prs.parse()
        result = []
        for exp in expression:
            tmp = interp.executor.interpret(exp)
            print(tmp)
            if tmp is not None:
                result.append(tmp)
        print(result)
        self.assertEqual(result, 30.0)

if __name__ == '__main__':
    unittest.main()
