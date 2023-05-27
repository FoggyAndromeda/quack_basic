import tokenizer.tokenizer as tokenizer
import customparser.parser as parser
from expressions.visitor import Executor


class Interpreter:

    def __init__(self):
        self.executor = Executor()

    def run_file(self, path: str):
        try:
            file = open(path)
            for line in file:
                self.run(line)
        except FileNotFoundError as e:
            print(f"Error in Interpreter: File {path} doesn't exist\n{e}")
        except Exception as e:
            print(f"Error in Interpreter: {e}")

    def run_repl(self):
        pass

    def run(self, src: str):
        tkn = tokenizer.Tokenizer(src)
        tokens = tkn.to_tokens()

        # for t in tokens:
        #     print(t)

        prs = parser.Parser(tokens)
        expression = prs.parse()

        if expression == None:
            return

        self.executor.interpret(expression)
