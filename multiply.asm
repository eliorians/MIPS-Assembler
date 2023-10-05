# This function computes integer multiplication
#
        daddi r1 r0 num1a
        daddi r2 r0 num1b
        daddi r3 r0 result1
        daddi r4 r0 0
        daddi r5 r0 5
loop    ld r6 0 r1
        ld r7 0 r2
        daddi r8 r0 0            # set r8 to 0
inner   dadd r8 r8 r6
        daddi r7 r7 -1
        bne r7 r0 inner
        sd r8 0 r3
        daddi r1 r1 24
        daddi r2 r2 24
        daddi r3 r3 24
        daddi r4 r4 1
        bne r4 r5 loop
        halt
num1a   .dfill 1
num1b   .dfill 2
result1 .dfill 0
num2a   .dfill 3
num2b   .dfill 2
result2 .dfill 0
num3a   .dfill 4
num3b   .dfill 5
result3 .dfill 0
num4a   .dfill 4
num4b   .dfill 3
result4 .dfill 0
num5a   .dfill 4
num5b   .dfill 1
result5 .dfill 0
