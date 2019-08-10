greeting: bytes[20]
index: uint256

@public
def __init__(_greeting: bytes[20], _number: uint256):
    self.greeting = _greeting
    self.index = _number

@public
def greet() -> bytes[20]:
    return self.greeting

@public
def get_index() -> uint256:
    return self.index
