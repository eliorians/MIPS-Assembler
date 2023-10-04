    ld r3 num1a r0
    daddiu r5 r3 -2
    sd r5 resulta r0
#
    ld r3 num1b r0
    daddiu r5 r3 2
    sd r5 resultb r0
#
    ld r3 num1c r0
    daddiu r5 r3 -4
    sd r5 resultc r0
#
    ld r3 num1d r0
    daddiu r5 r3 4
    sd r5 resultd r0
#
    ld r3 num1e r0
    daddiu r5 r3 -6
    sd r5 resulte r0
#
    ld r3 num1f r0
    daddiu r5 r3 6
    sd r5 resultf r0
#
    halt
num1a .dfill 1
num1b .dfill 1
num1c .dfill 2
num1d .dfill 2
num1e .dfill 3
num1f .dfill 3
resulta .dfill 0
resultb .dfill 0
resultc .dfill 0
resultd .dfill 0
resulte .dfill 0
resultf .dfill 0
