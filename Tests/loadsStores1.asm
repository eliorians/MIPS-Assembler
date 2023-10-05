#
# loads and stores must be executed in the order
# in which they are issued
#
        l.d f0 here    r0
        ld r1 there r0
        ld r2 more r0
        ld r3 num1 r0
        ld r4 num2 r0
        ld r5 num3 r0
        sd r3 dest1 r0
        sd r4 dest2 r0
        sd r5 dest3 r0
        halt
here   .dfill 3.7
there  .dfill 2
more   .dfill 15
num1   .dfill -1
num2   .dfill 23
num3   .dfill 31
dest1  .dfill 0
dest2  .dfill 0
dest3  .dfill 0
