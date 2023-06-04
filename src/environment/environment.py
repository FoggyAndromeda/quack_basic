class Environment:

    def __init__(self):
        self.mp = {}

    def create_variable(self, name: str, value):
        self.mp[name] = value

    def change_variable(self, name: str, value):
        self.mp[name] = value

    def get_variable(self, name: str):
        return self.mp[name]

    def check_variable_existance(self, name: str):
        return name in self.mp
