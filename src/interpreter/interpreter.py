import tokenizer.tokenizer as tokenizer


class Interpreter:

    def __init__(self):
        pass

    def run_file(self, path: str):
        try:
            file = open(path)
            src = '\n'.join(file.readlines())
            self.run(src)
        except FileNotFoundError as e:
            print(f"File {path} doesn't exist\n{e}")
        except Exception as e:
            print(f"Something went wrong: {e}")

    def run_repl(self):
        pass

    def run(self, src: str):
        tkn = tokenizer.Tokenizer(src)
        tokens = tkn.to_tokens()

        for t in tokens:
            print(t)
