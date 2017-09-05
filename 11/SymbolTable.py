class SymbolTable:

    def __init__(self):
        self.globalScope = {}
        self.subroutinesScope = {}
        self.currScope = self.globalScope
        self.varCounter = 0
        self.argCounter = 0
        self.fieldCounter = 0
        self.staticCounter = 0
        self.ifCounter = 0
        self.whileCounter = 0

    def startSubroutine(self, name):
        self.subroutinesScope[name] = {}
        self.varCounter = 0
        self.argCounter = 0
        self.ifCounter = 0
        self.whileCounter = 0

    def define(self, name, type, kind):
        if kind == "static":
            self.globalScope[name] = (type, kind, self.staticCounter)
            self.staticCounter += 1
        elif kind == "field":
            self.globalScope[name] = (type, kind, self.fieldCounter)
            self.fieldCounter += 1
        elif kind == 'arg':
            self.currScope[name] = (type, kind, self.argCounter)
            self.argCounter += 1
        elif kind == 'var':
            self.currScope[name] = (type, kind, self.varCounter)
            self.varCounter += 1

    def globalsCount(self, kind):
        return len([v for (k, v) in self.globalScope.items() if v[1] == kind])

    def varCount(self, kind):
        return len([v for (k, v) in self.currScope.items() if v[1] == kind])

    def typeOf(self, name):
        if name in self.currScope:
            return self.currScope[name][0]
        if name in self.globalScope:
            return self.globalScope[name][0]
        else:
            return "NONE"

    def kindOf(self, name):
        if name in self.currScope:
            return self.currScope[name][1]
        if name in self.globalScope:
            return self.globalScope[name][1]
        else:
            return "NONE"

    def indexOf(self, name):
        if name in self.currScope:
            return self.currScope[name][2]
        if name in self.globalScope:
            return self.globalScope[name][2]
        else:
            return "NONE"

    def setScope(self, name):
        if name == 'global':
            self.currScope = self.globalScope
        else:
            self.currScope = self.subroutinesScope[name]
