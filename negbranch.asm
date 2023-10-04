# branches to statement above branch (negative offset)
# Also, tests to see if a negative dfill value can be generated
# properly
# Also tests to see if an immediate value can be handled 
# in the sd
	ld	r1	negone	r0	# r1 = -1
loop	daddi	r1	r1	1	# r1 = r1 + 1
	beq	r1	r0	loop	# if r1 == 0 goto loop
	nop
	sd	r1	32	r0	# m[32] = r1
	halt
negone	.dfill	-1
result	.dfill	0
