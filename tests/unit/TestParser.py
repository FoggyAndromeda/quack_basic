import unittest
from src.tokenizer.tokenizer import TokenType, Token, Tokenizer as tkn
from src.expressions.expressions import *
from src.customparser.parser import Parser

class TestParser(unittest.TestCase):
    def test_parse_empty(self):
        foo = tkn("")
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse(), None)
    def test_parse_number(self):
        foo = tkn("1")
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse().value, Literal(1.0).value)
    def test_parse_string(self):
        foo = tkn("\"aB\"")
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse().value, Literal('aB').value)



if __name__ == '__main__':
    unittest.main()
