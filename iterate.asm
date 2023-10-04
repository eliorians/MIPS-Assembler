#loop of code equivalent to:
#   sum = 0;
#   for (i = 0; i < 10; i++)
#      sum = sum + i
#
	ld	r1	sum	r0	# r[1] = 0
	ld	r2	ten	r0	# r[2] = 10
	daddi	r3	r0	0	# r[3] = 0
loop	dadd	r1	r1	r3	# r[1] = r[1] + r[3]
	daddi	r3	r3	1	# r[3] = r[3] + 1
	beq	r3	r2	end	#	if r[3] == r[2] goto end
	nop
	j	loop	# goto loop
	nop
end	halt
sum	.dfill	0
ten	.dfill	10
