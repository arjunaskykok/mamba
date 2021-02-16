"""
@title A greeting program
@author Arjuna Sky Kok
@notice You can use this contract for greeting
@dev Greetings must be done in a polite way
"""
greeting: String[20]

@external
def __init__():
    self.greeting = "Hello World"

@external
def setGreeting(x: String[20]):
    """
    @notice Set the greeting
    @dev Set the greeting no less than 20 bytes
    @param x The greeting itself
    """
    self.greeting = x

@external
def greet() -> String[20]:
    """
    @notice Return the greeting
    @dev Return the greeting which is 20 bytes
    @return The greeting itself
    """
    return self.greeting
