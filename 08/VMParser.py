import re

class Parser(object):

    C_ARITHMETIC = 0 
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    C_IF = 5
    C_FUNCTION = 6
    C_RETURN = 7
    C_CALL = 8

    def __init__(self, input_file):
        with open(input_file, "r+") as f:
            self.lines = f.readlines()
        self.command = ""
        self.current_line = 0

    def hasMoreCommands(self):
        if self.current_line <= (len(self.lines) - 1):
            return True
        else:
            return False

    def advance(self):
        self.command = self.lines[self.current_line]
        self.current_line += 1

    def commandType(self):
        if re.match(r'(\s|^|$)push(\s|^|$)', self.command, flags=re.IGNORECASE): #searches exact word
            return Parser.C_PUSH
        elif re.match(r'(\s|^|$)pop(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_POP
        elif re.match(r'(\s|^|$)label(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_LABEL
        elif re.match(r'(\s|^|$)goto(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_GOTO
        elif re.match(r'(\s|^|$)if-goto(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_IF
        elif re.match(r'(\s|^|$)function(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_FUNCTION
        elif re.match(r'(\s|^|$)return(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_RETURN
        elif re.match(r'(\s|^|$)call(\s|^|$)', self.command, flags=re.IGNORECASE):
            return Parser.C_CALL
        else:
            return Parser.C_ARITHMETIC

    def arg1(self):
        splitC = self.command.split()
        if self.commandType() == Parser.C_ARITHMETIC:
            return splitC[0]
        elif self.commandType() == Parser.C_RETURN:
            return "RETURN has no arguments."
        else:
            return splitC[1]

    def arg2(self):
        splitC = self.command.split()
        return splitC[2]
