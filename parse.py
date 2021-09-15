import sys
from lexer import *

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer):
        self.lexer=lexer
        self.curToken=None
        self.peekToken=None
        self.nextToken()
        self.nextToken()

    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def program(self):
        print("PROGRAM")
        while not self.checkToken(TokenType.EOF):
            self.statement()
    def statement(self):
        # Check the first token to see what kind of statement this is.

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()
            if self.checkToken(TokenType.STRING):
                self.nextToken()
            else:
                # Expect an expression.
                self.expression()
        
        self.nl()
    def nl(self):
        print("NEWLINE")
        print(self.curToken.kind)
        self.match(TokenType.NEWLINE)

        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
    def abort(self, message):
        sys.exit("Error. " + message)