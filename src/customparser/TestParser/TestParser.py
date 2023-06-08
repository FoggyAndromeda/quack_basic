import unittest

from expressions import *
from statements import *
from tokenizer import TokenType, Token, Tokenizer as tkn

from parser import Parser


class TestParser(unittest.TestCase):
    def test_parse_empty(self):
        foo = tkn("")
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse(), [])
    def test_parse_number(self):
        foo = tkn("""1
                     """)
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse()[0].expr.value, ExpressionStatement(Literal(1.0)).expr.value)
    def test_parse_string(self):
        foo = tkn("""\"aB\"
                     """)
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse()[0].expr.value, ExpressionStatement(Literal('aB')).expr.value)
    def test_parse_print(self):
        foo = tkn("""PRINT 10
                     """)
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse()[0].expr[0].value,
                         PrintStatement(Literal(10)).expr.value)


if __name__ == '__main__':
    unittest.main()
