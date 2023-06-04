class Environment:

    def __init__(self):
        self.values = {}

    def create_variable(self, name: str, value):
        self.values[name] = value

    def change_variable(self, name: str, value):
        self.values[name] = value

    def get_variable(self, name: str):
        return self.values[name]

    def check_variable_existance(self, name: str):
        return name in self.values
