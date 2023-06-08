import unittest

import tokenizer as tkn


class TestTokenizer(unittest.TestCase):
    def test_to_tokens_empty(self):
        foo = tkn.Tokenizer("")
        bar = foo.to_tokens()
        self.assertEqual(str(bar[0]), "EOF")
    def test_to_tokens_number(self):
        foo = tkn.Tokenizer("1")
        bar = foo.to_tokens()
        self.assertEqual(str(bar[0]), "NUMBER 1 1.0")
    def test_to_tokens_string(self):
        foo = tkn.Tokenizer("\"aB\"")
        bar = foo.to_tokens()
        self.assertEqual(str(bar[0]), 'STRING "aB" aB')
    def test_to_tokens_print(self):
        foo = tkn.Tokenizer("PRINT 10")
        bar = foo.to_tokens()
        self.assertEqual([str(a) for a in bar[0:2]], ['PRINT', 'NUMBER 10 10.0'])

if __name__ == '__main__':
    unittest.main()
