import os

class CodeWriter(object):

    def __init__(self, input_file):
        self.VM = ""
        self.a = open(input_file, 'w')
        self.label = 0
        self.uniquelabel = []
        self.currentFunction = ""

    def setFileName(self, fileName):
        self.VM, ext = os.path.splitext(fileName)

    def close(self):
        self.a.close()

    def writeInit(self):
        self.a.write("// Bootstrap\n")
        self.a_command("256")
        self.c_command("D", "A", None)
        self.a_command("SP")
        self.c_command("M", "D", None)
        self.writeCall("Sys.init", 0)

    def writeLabel(self, label):
        if label not in self.uniquelabel:
            newLabel = self.currentFunction + "$" + label
            self.addUniqueLabel(newLabel)
            self.a.write("\n // " + label + "\n")
            self.loop(newLabel)
        else:
            self.loop(label)

    def writeGoto(self, label):
        self.a.write("\n // " + "goto " + label + "\n")
        if label in self.uniquelabel:
            self.a_command(label)
            self.c_command(None, "0", "JMP")
        else:
            newLabel = self.currentFunction + "$" + label
            self.addUniqueLabel(newLabel)
            self.a_command(newLabel)
            self.c_command(None, "0", "JMP")

    def writeIf(self, label):
        self.a.write("\n // " + "if-goto " + label + "\n")
        if label in self.uniquelabel:
            self.a_command("SP")
            self.c_command("AM", "M-1")
            self.c_command("D", "M")
            self.a_command(label)
            self.c_command(None, "D", "JNE")
        else:
            newLabel = self.addUniqueLabel(self.currentFunction + "$" + label)
            self.a_command("SP")
            self.c_command("AM", "M-1")
            self.c_command("D", "M")
            self.a_command(newLabel)
            self.c_command(None, "D", "JNE")

    def writeCall(self, functionName, numArgs):
        self.currentFunction = functionName
        RETURN_ADDRESS = self.getUniqueLabel(self.currentFunction + "$" + "RETURN")
        self.a.write("\n// " + functionName  + " " + str(numArgs) + "\n")
        self.a_command(RETURN_ADDRESS)
        self.equals("D", "A")
        self.a_command("SP")
        self.equals("A", "M")
        self.equals("M", "D")
        self.a_command("SP")
        self.equals("M", "M+1")

        self.pushTemp_yesP("LCL", 0);
        self.pushTemp_yesP("ARG", 0);
        self.pushTemp_yesP("THIS", 0);
        self.pushTemp_yesP("THAT", 0);

        self.equals("D", "M")
        self.a_command("5")
        self.equals("D", "D-A")
        self.a_command(numArgs)
        self.equals("D", "D-A")
        self.a_command("ARG")
        self.equals("M", "D")
        self.a_command("SP")
        self.equals("D", "M")
        self.a_command("LCL")
        self.equals("M", "D")
        self.a_command(functionName)
        self.c_command(None, "0", "JMP")
        self.loop(RETURN_ADDRESS)

    def writeReturn(self):
        self.a.write("\n // " + "return\n")
        self.a_command("LCL")
        self.equals("D", "M")
        self.a_command("R15")
        self.equals("M", "D")

        self.a_command("5")
        self.equals("A", "D-A")
        self.equals("D", "M")
        self.a_command("R14")
        self.equals("M", "D")

        self.a_command("SP")
        self.equals("AM", "M-1")
        self.equals("D", "M")
        self.a_command("ARG")
        self.c_command("A", "M")
        self.equals("M", "D")

        self.a_command("ARG")
        self.equals("M", "M+1")
        self.equals("D", "M")
        self.a_command("SP")
        self.equals("M", "D")

        self.preTemplate("THAT")
        self.preTemplate("THIS")
        self.preTemplate("ARG")
        self.preTemplate("LCL")

        self.a_command("R14")
        self.equals("A", "M")
        self.c_command(None, "0", "JMP")

    def writeFunction(self, functionName, numLocals):
        self.currentFunction = functionName
        self.addUniqueLabel(functionName)
        self.a.write("\n// " + functionName + " " + str(numLocals) + "\n")
        self.loop(self.currentFunction)
        for i in range(0, int(numLocals)):
            self.writePushPop(1, "constant", 0)

    def preTemplate(self, pos):
        self.a_command("R15")
        self.equals("D", "M-1")
        self.equals("AM", "D")
        self.equals("D", "M")
        self.a_command(pos)
        self.equals("M", "D")

    def writeArithmetic(self, command):
        self.a.write("\n // " + command + "\n")
        if command == "sub":
            self.arithmeticTemp()
            self.equals("M", "M-D")
        elif command == "add":
            self.arithmeticTemp()
            self.equals("M", "M+D")
        elif command == "or":
            self.arithmeticTemp()
            self.equals("M", "D|M")
        elif command == "and":
            self.arithmeticTemp()
            self.equals("M", "D&M")
        elif command == "not":
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "!M")
        elif command == "neg":
            self.equals("D", "0")
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "D-M")
        elif command == "gt":
            self.arithmeticTemp()
            self.equals("D", "M-D")
            FALSE_gt = self.getUniqueLabel("FALSE_gt")
            self.a_command(FALSE_gt)
            self.c_command(None, "D", "JLE")
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "-1")
            CONTINUE_gt = self.getUniqueLabel("CONTINUE_gt")
            self.a_command(CONTINUE_gt)
            self.c_command(None, "0", "JMP")
            self.loop(FALSE_gt)
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "0")
            self.loop(CONTINUE_gt)
        elif command == "eq":
            self.arithmeticTemp()
            self.equals("D", "M-D")
            FALSE_eq = self.getUniqueLabel("FALSE_eq")
            self.a_command(FALSE_eq)
            self.c_command(None, "D", "JNE")
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "-1")
            CONTINUE_eq = self.getUniqueLabel("CONTINUE_eq")
            self.a_command(CONTINUE_eq)
            self.c_command(None, "0", "JMP")
            self.loop(FALSE_eq)
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "0")
            self.loop(CONTINUE_eq)
        elif command == "lt":
            self.arithmeticTemp()
            self.equals("D", "M-D")
            FALSE_lt = self.getUniqueLabel("FALSE_lt")
            self.a_command(FALSE_lt)
            self.c_command(None, "D", "JGE")
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "-1")
            CONTINUE_lt = self.getUniqueLabel("CONTINUE_lt")
            self.a_command(CONTINUE_lt)
            self.c_command(None, "0", "JMP")
            self.loop(FALSE_lt)
            self.a_command("SP")
            self.equals("A", "M-1")
            self.equals("M", "0")
            self.loop(CONTINUE_lt)

    def writePushPop(self, command, segment, index):
        if command == 1:
            self.a.write("\n// " + "push " + segment + " " + str(index) + "\n")
            if segment == "constant":
                self.a_command(index)
                self.equals("D", "A")
                self.a_command("SP")
                self.equals("A", "M")
                self.equals("M", "D")
                self.a_command("SP")
                self.equals("M", "M+1")
            elif segment == "local":
                self.pushTemp_noP("LCL", index)
            elif segment == "argument":
                self.pushTemp_noP("ARG", index)
            elif segment == "this":
                self.pushTemp_noP("THIS", index)
            elif segment == "that":
                self.pushTemp_noP("THAT", index)
            elif segment == "pointer":
                if index == "0":
                    self.pushTemp_yesP("THIS", index)
                elif index == "1":
                    self.pushTemp_yesP("THAT", index)
            elif segment == "temp":
                self.a_command(index)
                self.equals("D", "A")
                self.a_command("5")
                self.equals("A", "A+D")
                self.equals("D", "M")
                self.a_command("SP")
                self.equals("A", "M")
                self.equals("M", "D")
                self.a_command("SP")
                self.equals("M", "M+1")
            elif segment == "static":
                self.a_command(self.VM + str(index))
                self.equals("D", "M")
                self.pushD_toSP()

        elif command == 2:
            self.a.write("\n// " + "pop " + segment + " " + str(index) +"\n")
            if segment == "local":
                self.popTemp_noP("LCL", index)
            elif segment == "argument":
                self.popTemp_noP("ARG", index)
            elif segment == "this":
                self.popTemp_noP("THIS", index)
            elif segment == "that":
                self.popTemp_noP("THAT", index)
            elif segment == "pointer":
                if index == "0":
                    self.popTemp_yesP("THIS", index)
                elif index == "1":
                    self.popTemp_yesP("THAT", index)
            elif segment == "temp":
                self.a_command(index)
                self.equals("D", "A")
                self.a_command("5")
                self.equals("D", "D+A")
                self.a_command("R13")
                self.equals("M", "D")
                self.a_command("SP")
                self.equals("AM", "M-1")
                self.equals("D", "M")
                self.a_command("R13")
                self.equals("A", "M")
                self.equals("M", "D")
            elif segment == "static":
                self.a_command(self.VM + str(index))
                self.equals("D", "A")
                self.a_command("R13")
                self.equals("M", "D")
                self.a_command("SP")
                self.equals("AM", "M-1")
                self.equals("D", "M")
                self.a_command("R13")
                self.equals("A", "M")
                self.equals("M", "D")
            else:
                print("Something is wrong")

    def arithmeticTemp(self):
        self.a_command("SP")
        self.equals("AM", "M-1")
        self.equals("D", "M")
        self.equals("A", "A-1")

    def pushTemp_yesP(self, segment, index):
        self.a_command(segment)
        self.equals("D", "M")
        self.pushD_toSP()

    def pushTemp_noP(self, segment, index):
        self.a_command(index)
        self.equals("D", "A")
        self.a_command(segment)
        self.equals("A", "M")
        self.equals("D", "D+A")
        self.equals("A", "D")
        self.equals("D", "M")
        self.pushD_toSP()

    def popTemp_yesP(self, segment, index):
        self.a_command("SP")
        self.equals("M", "M-1")
        self.equals("A", "M")
        self.equals("D", "M")
        self.a_command(segment)
        self.equals("M", "D")

    def popTemp_noP(self, segment, index):
        self.a_command(index)
        self.equals("D", "A")
        self.a_command(segment)
        self.equals("A", "M")
        self.equals("D", "D+A")
        self.a_command(segment)
        self.equals("M", "D")
        self.a_command("SP")
        self.equals("AM", "M-1")
        self.equals("D", "M")
        self.a_command(segment)
        self.equals("A", "M")
        self.equals("M", "D")
        self.a_command(index)
        self.equals("D", "A")
        self.a_command(segment)
        self.equals("A", "M")
        self.equals("D", "A-D")
        self.a_command(segment)
        self.equals("M", "D")

    def pushD_toSP(self):
        self.a_command("SP")
        self.equals("A", "M")
        self.equals("M", "D")
        self.a_command("SP")
        self.equals("M", "M+1")

    def equals(self, left, right):
        self.a.write(left + "=" + right + "\n")

    def loop(self, item):
        self.a.write("(" + item + ")" + "\n")

    def a_command(self, address):
        address = str(address)
        self.a.write("@" + address + "\n")

    def c_command(self, dest, comp, jump = None):
        if dest != None and jump == None:
            self.a.write(dest + "=" + comp)
        elif dest == None and jump != None:
            self.a.write(comp + ";" + jump)
        elif dest != None and jump != None:
            self.a.write(dest + "=" + comp + ";" + jump)
        elif dest == None and jump == None:
            self.a.write(comp)
        self.a.write("\n")

    def getUniqueLabel(self, oldLabel):
        self.label += 1
        unique = oldLabel + str(self.label)
        self.uniquelabel.append(unique)
        return unique

    def addUniqueLabel(self, label):
        self.uniquelabel.append(label)
        return label
