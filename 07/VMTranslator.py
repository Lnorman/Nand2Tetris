import os, sys
from VMParser import *
from VMCodewriter import *

def main():
  root = sys.argv[1]
  parser = Parser(root + ".vm")
  writer = CodeWriter(root + ".asm")

  while parser.hasMoreCommands():
    parser.advance()
    cType = parser.commandType()
    if cType == "push" or cType == "pop":
      writer.writePushPop(cType, parser.arg1(), parser.arg2())
    elif cType == "arithmetic":
      writer.writeArithmetic(parser.command[0])
    else:
      writer.writeError()

if __name__ == "__main__":
  main()
