    ld r3 num1a r0
    ld r4 num2a r0
    dadd r5 r3 r4
    sd r5 resulta r0
#
    ld r3 num1b r0
    ld r4 num2b r0
    dadd r5 r3 r4
    sd r5 resultb r0
#
    ld r3 num1c r0
    ld r4 num2c r0
    dadd r5 r3 r4
    sd r5 resultc r0
#
    ld r3 num1d r0
    ld r4 num2d r0
    dadd r5 r3 r4
    sd r5 resuld r0
#
    ld r3 num1e r0
    ld r4 num2e r0
    dadd r5 r3 r4
    sd r5 resulte r0
#
    ld r3 num1f r0
    ld r4 num2f r0
    dadd r5 r3 r4
    sd r5 resultf r0
#
    halt
num1a .dfill 1
num1b .dfill 2
num1c .dfill 3
num1d .dfill 4
num1e .dfill 5
num1f .dfill 6
num2a .dfill 2
num2b .dfill 3
num2c .dfill 4
num2d .dfill 5
num2e .dfill 6
num2f .dfill 7
resulta .dfill 0
resultb .dfill 0
resultc .dfill 0
resuld .dfill 0
resulte .dfill 0
resultf .dfill 0
