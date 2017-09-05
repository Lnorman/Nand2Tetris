import JackTokenizer


class CompilationEngine(object):

    binaryOp = {'+', '-', '*', '/', '|', '=', '&lt;', '&gt;', '&amp;'}
    unaryOp = {'-', '~'}
    keywordConstant = {'true', 'false', 'null', 'this'}

    def __init__(self, input, output):
        self.tokenizer = JackTokenizer.JackTokenizer(input)
        self.parsedRules = []
        self.outputFile = open(output, 'w')
        self.indent = ""

    def addIndent(self):
        self.indent += "    "

    def deleteIndent(self):
        self.indent = self.indent[:-4]

    def writeNonTerminalStart(self, rule):
        self.outputFile.write(self.indent+"<"+rule+">\n")
        self.parsedRules.append(rule)
        self.addIndent()

    def writeNonTerminalEnd(self):
        self.deleteIndent()
        rule = self.parsedRules.pop()
        self.outputFile.write(self.indent+"</"+rule+">\n")

    def writeTerminal(self, token, value):
        self.outputFile.write(self.indent+"<"+token+"> "+value+" </"+token+">\n")

    def advance(self):
        token, value = self.tokenizer.advance()
        self.writeTerminal(token, value)

    def nextValueIn(self, list):
        token, value = self.tokenizer.peek()
        return value in list

    def nextValueIs(self, val):
        token, value = self.tokenizer.peek()
        return value == val

    def nextTokenIs(self, tok):
        token, value = self.tokenizer.peek()
        return token == tok

    def compileClass(self):
        self.writeNonTerminalStart('class')
        self.advance()
        self.advance()
        self.advance()
        if self.existClassVarDec():
            self.compileClassVarDec()
        while self.existSubroutine():
            self.compileSubroutine()
        self.advance()
        self.writeNonTerminalEnd()
        self.outputFile.close()

    def existClassVarDec(self):
        return self.nextValueIs("static") or self.nextValueIs("field")

    def existSubroutine(self):
        return self.nextValueIs("constructor") or self.nextValueIs("method")\
               or self.nextValueIs("function")

    def compileClassVarDec(self):
        while self.existClassVarDec():
            self.writeNonTerminalStart('classVarDec')
            self.writeClassVarDec()
            self.writeNonTerminalEnd()

    def writeClassVarDec(self):
        self.advance()
        self.advance()
        self.advance()
        while self.nextValueIs(","):
            self.advance()
            self.advance()
        self.advance()

    def compileSubroutine(self):
        self.writeNonTerminalStart('subroutineDec')
        self.advance()
        self.advance()
        self.advance()
        self.advance()
        self.compileParameterList()
        self.advance()
        self.compileSubroutineBody()
        self.writeNonTerminalEnd()


    def compileParameterList(self):
        self.writeNonTerminalStart('parameterList')
        while self.existParameter():
            self.writeParam()
        self.writeNonTerminalEnd()

    def existParameter(self):
        return not self.nextTokenIs("symbol")

    def writeParam(self):
        self.advance()
        self.advance()
        if self.nextValueIs(","):
            self.advance()


    def compileSubroutineBody(self):
        self.writeNonTerminalStart('subroutineBody')
        self.advance()
        while self.existVarDec():
            self.compileVarDec()
        self.compileStatements()
        self.advance()
        self.writeNonTerminalEnd()

    def existVarDec(self):
        return self.nextValueIs("var")

    def compileVarDec(self):
        self.writeNonTerminalStart('varDec')
        self.advance()
        self.advance()
        self.advance()
        while self.nextValueIs(","):
            self.advance()
            self.advance()
        self.advance()
        self.writeNonTerminalEnd()

    def compileStatements(self):
        self.writeNonTerminalStart('statements')
        while self.existStatement():
            if   self.nextValueIs("do"):     self.compileDo()
            elif self.nextValueIs("let"):    self.compileLet()
            elif self.nextValueIs("if"):     self.compileIf()
            elif self.nextValueIs("while"):  self.compileWhile()
            elif self.nextValueIs("return"): self.compileReturn()
        self.writeNonTerminalEnd()

    def existStatement(self):
        return self.nextValueIs("do") \
            or self.nextValueIs("let")\
            or self.nextValueIs("if")\
            or self.nextValueIs("while")\
            or self.nextValueIs("return")\

    def compileDo(self):
        self.writeNonTerminalStart('doStatement')
        self.advance()
        self.compileSubroutineCall()
        self.advance()
        self.writeNonTerminalEnd()

    def compileSubroutineCall(self):
        self.advance()
        if self.nextValueIs("."):
            self.advance()
            self.advance()
        self.advance()
        self.compileExpressionList()
        self.advance()

    def compileExpressionList(self):
        self.writeNonTerminalStart('expressionList')
        if self.existExpression():
            self.compileExpression()
        while self.nextValueIs(","):
            self.advance()
            self.compileExpression()
        self.writeNonTerminalEnd()

    def compileLet(self):
        self.writeNonTerminalStart('letStatement')
        self.advance()
        self.advance()
        if self.nextValueIs("["):
            self.writeArrayIndex()
        self.advance()
        self.compileExpression()
        self.advance()
        self.writeNonTerminalEnd()

    def writeArrayIndex(self):
        self.advance()
        self.compileExpression()
        self.advance()

    def compileWhile(self):
        self.writeNonTerminalStart('whileStatement')
        self.advance()
        self.advance()
        self.compileExpression()
        self.advance()
        self.advance()
        self.compileStatements()
        self.advance()
        self.writeNonTerminalEnd()

    def compileReturn(self):
        self.writeNonTerminalStart('returnStatement')
        self.advance()
        while self.existExpression():
            self.compileExpression()
        self.advance()
        self.writeNonTerminalEnd()

    def existExpression(self):
        return self.existTerm()

    def existTerm(self):
        token, value = self.tokenizer.peek()
        return self.nextTokenIs("integerConstant") or self.nextTokenIs("stringConstant")\
               or self.nextTokenIs("identifier") or (self.nextValueIn(self.unaryOp))\
               or (self.nextValueIn(self.keywordConstant)) or (self.nextValueIs('('))

    def compileIf(self):
        self.writeNonTerminalStart('ifStatement')
        self.advance()
        self.advance()
        self.compileExpression()
        self.advance()
        self.advance()
        self.compileStatements()
        self.advance()
        if self.nextValueIs("else"):
            self.advance()
            self.advance()
            self.compileStatements()
            self.advance()
        self.writeNonTerminalEnd()

    def compileExpression(self):
        self.writeNonTerminalStart('expression')
        self.compileTerm()
        while self.nextValueIn(self.binaryOp):
            self.advance()
            self.compileTerm()
        self.writeNonTerminalEnd()

    def compileTerm(self):
        self.writeNonTerminalStart('term')
        if self.nextTokenIs("integerConstant") or self.nextTokenIs("stringConstant")\
                or (self.nextValueIn(self.keywordConstant)):
            self.advance()
        elif self.nextTokenIs("identifier"):
            self.advance()
            if self.nextValueIs("["):
                self.writeArrayIndex()
            if self.nextValueIs("("):
                self.advance()
                self.compileExpressionList()
                self.advance()
            if self.nextValueIs("."):
                self.advance()
                self.advance()
                self.advance()
                self.compileExpressionList()
                self.advance()
        elif self.nextValueIn(self.unaryOp):
            self.advance()
            self.compileTerm()
        elif self.nextValueIs("("):
            self.advance()
            self.compileExpression()
            self.advance() 
        self.writeNonTerminalEnd()
