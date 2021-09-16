from lexer import *
from parse import *
from emitter import *
import sys

def main():
    print("Roar Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer,emitter)

    parser.program() # Start the parser.
    print("Parsing completed.")

main()