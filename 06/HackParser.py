import re

class Parser(object):

    _comment = re.compile(r'//.*$')

    def __init__(self, filename):
        self.command = ''
        with open(filename, 'r') as myf:
            self.lines = myf.readlines()
        self.current_line = -1

    def hasMoreCommands(self):
        return self.current_line < len(self.lines) - 1

    def advance(self):
        self.current_line += 1
        line = self.lines[self.current_line]
        line = self._comment.sub('', line)
        if line == '\n':
            self.advance()
        else:
            self.command = line.strip()

    def command_type(self):
        if len(self.command) == 0:
            return None
        if re.match(r'^@.*', self.command):
            return 'A_COMMAND'
        elif re.match(r'^\(.*', self.command):
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        matching = re.match(r'^[@\(](.*?)\)?$', self.command)
        symbol = matching.group(1)
        return symbol

    def dest(self):
         if '=' in self.command:
             return self.command.split('=')[0]
         else:
             return 'null'
             
    def comp(self):
        comp = re.sub(r'^.*?=', '', self.command)
        comp = re.sub(r';\w+$', '', comp)
        return comp.strip()

    def jump(self):
        matching = re.match(r'^.*;(\w+)$', self.command)
        if not matching:
            jump = 'null'
        else:
            jump = matching.group(1)
        return jump
