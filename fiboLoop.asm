# This code computes the first 11 Fibonacci numbers
# and stores them in memory.
	ld	r1	fib0	r0	       #r1 = fib number 0
	ld	r2	fib1	r0         #r2 = fib number 1
    daddiu r3 r0    fib2       #address of fib2
    daddi  r4 r0    10         #top loop bounds
    daddiu r5 r0    0          #loop counter
loop   dadd	r6	r1	r2
	sd	r6  0		r3
	dadd	r1	r2	r0         # r1 = r2
	dadd	r2	r6	r0         # r2 = r6
    daddiu  r3 r3   8          #increment store address
    daddi   r5 r5   1          #increment loop counter
    bne  r5 r4    loop
    halt
fib0	.dfill	0
fib1	.dfill	1
fib2	.dfill	0
