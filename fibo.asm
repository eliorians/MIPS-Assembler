# This code computes the first 11 Fibonacci numbers
# and stores them in memory.
	ld	r1	fib0	r0	
	ld	r2	fib1	r0
	dadd	r3	r1	r2
	sd	r3	fib2	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib3	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib4	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib5	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib6	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib7	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib8	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib9	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib10	r0
	dadd	r1	r2	r0
	dadd	r2	r3	r0
	dadd	r3	r1	r2
	sd	r3	fib11	r0
    halt
fib0	.dfill	0
fib1	.dfill	1
fib2	.dfill	0
fib3	.dfill	0
fib4	.dfill	0
fib5	.dfill	0
fib6	.dfill	0
fib7	.dfill	0
fib8	.dfill	0
fib9	.dfill	0
fib10	.dfill	0
fib11	.dfill	0
