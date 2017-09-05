// Bootstrap
@256
D=A
@SP
M=D

// Sys.init 0
@Sys.init$RETURN1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$RETURN1)

// Main.fibonacci 0
(Main.fibonacci)

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

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

 // lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@FALSE_lt2
D;JGE
@SP
A=M-1
M=-1
@CONTINUE_lt3
0;JMP
(FALSE_lt2)
@SP
A=M-1
M=0
(CONTINUE_lt3)

 // if-goto IF_TRUE
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE

 // goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP

 // IF_TRUE
(Main.fibonacci$IF_TRUE)

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

 // IF_FALSE
(Main.fibonacci$IF_FALSE)

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

// push constant 2
@2
D=A
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

// Main.fibonacci 1
@Main.fibonacci$RETURN4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$RETURN4)

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

// push constant 1
@1
D=A
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

// Main.fibonacci 1
@Main.fibonacci$RETURN5
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$RETURN5)

 // add
@SP
AM=M-1
D=M
A=A-1
M=M+D

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
// Bootstrap
@256
D=A
@SP
M=D

// Sys.init 0
@Sys.init$RETURN6
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$RETURN6)

// Sys.init 0
(Sys.init)

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// Main.fibonacci 1
@Main.fibonacci$RETURN7
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$RETURN7)

 // WHILE
(Main.fibonacci$WHILE)

 // goto WHILE
@Main.fibonacci$WHILE
0;JMP
