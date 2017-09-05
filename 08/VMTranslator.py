import sys, glob, os
from VMParser import *
from VMCodewriter import *

class VMTranslator(object):

    def codeWriterTranslate(self, input_files, output_file):
        codeWriter = CodeWriter(output_file)
        for file in input_files:
            self.stripWhiteSpace(file)
            codeWriter.writeInit()
            self.parserTranslate(file, codeWriter)
        codeWriter.close()

    def parserTranslate(self, input_file, code_writer):
        parse = Parser(input_file)
        code_writer.setFileName(os.path.basename(input_file))
        while parse.hasMoreCommands():
            parse.advance()
            self.getASM(parse, code_writer)

    def stripWhiteSpace(self, input_file):
        with open(input_file, 'r+') as f:
            final_file = ""

            for line in f:
                if len(line.strip()) == 0:
                    continue
                else:
                    if line.partition('//')[1] == '//':
                        if line.partition('//')[0] != '':
                            line = line.partition('//')[0] + '\n'
                            line = line.replace('\t','')
                            final_file += line
                    else:
                        line = line.partition('//')[0]
                        line = line.replace('\t','')
                        final_file += line

            outputFile = input_file
            a = open(outputFile, 'w')
            a.write(final_file)

    def getASM(self, parser, code_writer):
        CT = parser.commandType()
        if CT == parser.C_ARITHMETIC:
            code_writer.writeArithmetic(parser.arg1())
        elif CT == parser.C_PUSH or CT == parser.C_POP:
            code_writer.writePushPop(CT, parser.arg1(), parser.arg2())
        elif CT == parser.C_LABEL:
            code_writer.writeLabel(parser.arg1())
        elif CT == parser.C_GOTO:
            code_writer.writeGoto(parser.arg1())
        elif CT == parser.C_IF:
            code_writer.writeIf(parser.arg1())
        elif CT == parser.C_RETURN:
            code_writer.writeReturn()
        elif CT == parser.C_FUNCTION:
            code_writer.writeFunction(parser.arg1(), parser.arg2())
        elif CT == parser.C_CALL:
            code_writer.writeCall(parser.arg1(), parser.arg2())

    def getFiles(self, files):
        if files.endswith(".vm"):
            return [files], files.replace(".vm", ".asm")
        else:
            self.filelist = []
            self.filelist += glob.glob(files + "/*.vm")
            asmfile = files + ".asm"
            return self.filelist, asmfile

def main():
    translateFiles = VMTranslator()
    inF, outF = translateFiles.getFiles(sys.argv[-1])
    translateFiles.codeWriterTranslate(inF, outF)



main()
