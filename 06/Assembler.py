import sys
from HackParser import *
from HackCode import *
from SymbolTable import *

class Assembler(object):

    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.symbol_table = SymbolTable()
        self.symbol_address = 16

    def pass1(self):
        parser = Parser(self.in_file)
        current_address = 0
        while (parser.hasMoreCommands()):
            parser.advance()
            if parser.command_type() == 'A_COMMAND' or 'C_COMMAND':
                current_address += 1
            elif parser.command_type() == 'L_COMMAND':
                self.symbol_table.addEntry(parser.symbol(), current_address)

    def pass2(self):
        parser = Parser(self.in_file)
        outf = open(self.out_file, 'w')
        code = Code()
        while (parser.hasMoreCommands()):
            parser.advance()
            if parser.command_type() == 'C_COMMAND':
                outf.write(code.gen_c_code(parser.comp(), parser.dest(), parser.jump()) + '\n')
            elif parser.command_type() == 'A_COMMAND':
                outf.write(code.gen_a_code(self.get_address(parser.symbol())) + '\n')
            elif parser.command_type() == 'L_COMMAND':
                pass
        outf.close()

    def get_address(self, symbol):
        if symbol.isdigit():
            return symbol
        else:
            if not self.symbol_table.contains(symbol):
                self.symbol_table.addEntry(symbol, self.symbol_address)
                self.symbol_address += 1
            return self.symbol_table.getAddress(symbol)

def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    asm = Assembler(in_file, out_file)
    asm.pass1()
    asm.pass2()

main()
