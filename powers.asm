#  This program calculates each set of base to the exponent 
#
        daddi r1 r0 0        # loop control variable
        daddi r2 r0 5        # loop upper bound
        daddiu r3 r0 base0   # address of first base
        daddiu r4 r0 exp0    # address of first exponent
        daddiu r5 r0 result0 # address of first result
loop    l.d f0 0 r3          # base
        ld  r6 0 r4          # exponent
        l.d f1 one r0        # result
inner   beq r6 r0 cont       # check to see if done
        mul.d f1 f1 f0       # result = result * base
        daddi r6 r6 -1       # subtract one from exponent
        j inner
cont    s.d f1 0 r5          # store result
        daddiu r3 r3 24      # increment base address
        daddiu r4 r4 24      # increment exponent address
        daddiu r5 r5 24      # increment result address
        daddi r1 r1 1        # add 1 to loop control variable
        bne r1 r2 loop
        halt
one      .dfill    1.0
base0    .dfill    3.2
exp0     .dfill    0
result0  .dfill    0
base1    .dfill    3.7
exp1     .dfill    1
result1  .dfill    0
base2    .dfill    4.2
exp2     .dfill    2
result2  .dfill    0
base3    .dfill    5.2
exp3     .dfill    3
result3  .dfill    0
base4    .dfill    10.0
exp4     .dfill    4
result4  .dfill    0
