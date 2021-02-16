greeting: String[20]
index: uint256

@external
def __init__(_greeting: String[20], _number: uint256):
    self.greeting = _greeting
    self.index = _number

@external
def greet() -> String[20]:
    return self.greeting

@external
def get_index() -> uint256:
    return self.index
