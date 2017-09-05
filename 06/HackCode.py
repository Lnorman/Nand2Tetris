class Code(object):

    jumpTable = { 'null': '000',
                  'JGT' : '001',
                  'JEQ' : '010',
                  'JEQ' : '010',
                  'JGE' : '011',
                  'JLT' : '100',
                  'JNE' : '101',
                  'JLE' : '110',
                  'JMP' : '111'
                  }

    compTable = { '0'   : '0101010',
                  '1'   : '0111111',
                  '-1'  : '0111010',
                  'D'   : '0001100',
                  'A'   : '0110000',
                  'M'   : '1110000',
                  '!D'  : '0001101',
                  '!A'  : '0110001',
                  '!M'  : '1110001',
                  '-D'  : '0001111',
                  '-A'  : '0110011',
                  '-M'  : '1110011',
                  'D+1' : '0011111',
                  'A+1' : '0110111',
                  'M+1' : '0110111',
                  'D-1' : '0001110',
                  'A-1' : '0110010',
                  'M-1' : '1110010',
                  'D+A' : '0000010',
                  'D+M' : '1000010',
                  'D-A' : '0010011',
                  'D-M' : '1010011',
                  'A-D' : '0000111',
                  'M-D' : '1000111',
                  'D&A' : '0000000',
                  'D&M' : '1000000',
                  'D|A' : '0010101',
                  'D|M' : '1010101'
                  }

    destTable = { 'null': '000',
                  'M': '001',
                  'D': '010',
                  'MD': '011',
                  'A': '100',
                  'AM': '101',
                  'AD': '110',
                  'AMD': '111'
                  }

    def __init__(self):
        pass

    def gen_a_code(self, address):
        return '0' + self._bits(address).zfill(15)

    def gen_c_code(self, comp, dest, jump):
        return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)

    def dest(self, command):
        return self.destTable[command]

    def comp(self, command):
        return self.compTable[command]

    def jump(self, command):
        return self.jumpTable[command]

    def _bits(self, num):
        return bin(int(num))[2:]
