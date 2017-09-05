
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 0
@0
D=A
@LCL
A=M
D=D+A
@LCL
M=D
@SP
AM=M-1
D=M
@LCL
A=M
M=D
@0
D=A
@LCL
A=M
D=A-D
@LCL
M=D

 // LOOP_START
($LOOP_START)

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

 // add
@SP
AM=M-1
D=M
A=A-1
M=M+D

// pop local 0
@0
D=A
@LCL
A=M
D=D+A
@LCL
M=D
@SP
AM=M-1
D=M
@LCL
A=M
M=D
@0
D=A
@LCL
A=M
D=A-D
@LCL
M=D

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

// pop argument 0
@0
D=A
@ARG
A=M
D=D+A
@ARG
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@0
D=A
@ARG
A=M
D=A-D
@ARG
M=D

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

 // if-goto LOOP_START
@SP
AM=M-1
D=M
@$LOOP_START
D;JNE

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
