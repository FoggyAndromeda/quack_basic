import unittest
import src.tokenizer.tokenizer as tokenizer
import src.customparser.parser as parser
from src.expressions.visitor import Executor
from src.interpreter.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def test_run_addition(self):
        interp = Interpreter()
        src = """
        
        """

if __name__ == '__main__':
    unittest.main()
