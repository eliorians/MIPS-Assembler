#  code equivalent to iterate.asm except that 
#  immediate values are used in the beq and
#  the j
	ld	r1	sum	r0	# r[1] = 0
	ld	r2	ten	r0	# r[2] = 10
	daddi	r3	r0	0	# r[3] = 0
loop	dadd	r1	r1	r3	# r[1] = r[1] + r[3]
	daddi	r3	r3	1	# r[3] = r[3] + 1
	beq	r3	r2	1	#	if r[3] == r[2] goto 1 instruction away from PC (end)
	nop
	j	3	# goto instruction number 3 (loop)
	nop
end	halt
sum	.dfill	0
ten	.dfill	10
