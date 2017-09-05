
// SimpleFunction.test 2
(SimpleFunction.test)

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push local 0
@0
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@1
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

 // add
@SP
AM=M-1
D=M
A=A-1
M=M+D

 // not
@SP
A=M-1
M=!M

// push argument 0
@0
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

 // add
@SP
AM=M-1
D=M
A=A-1
M=M+D

// push argument 1
@1
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

 // sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

 // return
@LCL
D=M
@R15
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
M=M+1
D=M
@SP
M=D
@R15
D=M-1
AM=D
D=M
@THAT
M=D
@R15
D=M-1
AM=D
D=M
@THIS
M=D
@R15
D=M-1
AM=D
D=M
@ARG
M=D
@R15
D=M-1
AM=D
D=M
@LCL
M=D
@R14
A=M
0;JMP
