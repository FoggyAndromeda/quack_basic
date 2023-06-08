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
        self.assertEqual(abc.parse()[0], (Literal('1.0')))
    def test_parse_string(self):
        foo = tkn("""\"aB\"
                     """)
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse()[0], Literal('aB'))
    def test_parse_print(self):
        foo = tkn("""PRINT 10
                     """)
        bar = foo.to_tokens()
        abc = Parser(bar)
        self.assertEqual(abc.parse()[0].expr,
                         PrintStatement(Unary(Token(TokenType.PRINT, "PRINT", "10", 0),
                                              Literal("10"))))


if __name__ == '__main__':
    unittest.main()
