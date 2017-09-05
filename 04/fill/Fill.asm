// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    (RESTART)    // Set up variable to hold the address of Ram[16384]
        @SCREEN // Load SCREEN into A register (RAM[16384])
        D=A     // D = address of SCREEN
        @pixl_addr      // Load 0 in A register
        M=D     // Memory[0] = address of SCREEN

    (KBDCHECK)   // Check if key is pressed or not
        @KBD     // Load KBD into A register
        D=M      // D = Memory[KBD]

        @BLACK   // Set jump target to BLACK
        D;JNE    // If D != 0, jump to BLACK

        @WHITE   // Set jump target to WHITE
        D;JMP    // else, jump to WHITE

    (BLACK)     // Give variable black color value
        @color      // Variable to hold value for screen color
        M=-1    // Black
        @INC    // Set jump target to INC
        0;JMP   // Unconditional jump to INC

    (WHITE)     // Give variable white color value
        @color      // Variable to hold value for screen color
        M=0     // White
        @INC    // Set jump target to INC
        0;JMP   // Unconditional jump to INC

    (INC)       // Fill each pixel with color
        @color      // Load screen color into A register
        D=M     // Pass screen color to D register
        @pixl_addr      // Load 0 into A register
        A=M     // Get address of pixel (Memory[0] = address of pixel)
        M=D     // Fill pixel with color

        @pixl_addr      // Load 0 into A register
        D=M+1     // D = next pixel address
        @KBD    // Load KBD into A register
        D=A-D   // Make sure we stop after 8192 pixels

        @pixl_addr      // Load 0 into A register
        M=M+1   // Inc to next pixel

        @INC    // Set jump target to INC
        D;JGT   // If D > 0 loop
        @RESET  // Set jump target to RESET
        D;JEQ   // Jump if D = 0

    (RESET)     // If key remains pressed, keep screen black. If not, reset.
        @KBD    // Load KBD into A register
        D=M     // D = Memory[KBD]

        @BLACK  // Set jump target to RESET
        0;JNE   // If D!=0, jump to RESET
        @RESTART // Set jump target to SCREEN
        0;JMP   // else, restart
