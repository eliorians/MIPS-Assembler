#will add the frist 10 natural numbers
#ten time a piece
	ld	r1	zero	r0
	ld	r2	one	r0
	ld	r3	two	r0
	ld	r4	three	r0
	ld	r5	four	r0
	ld	r6	five	r0
	ld	r7	six	r0
	ld	r8	seven	r0
	ld	r9	eight	r0
	ld	r10	nine	r0
	ld	r11	ten	r0
	ld	r20	0	r0
loop	dadd	r1	r1	r1	# r[1] = r[1] + r[3]
	daddi	r20	r20	1	# r[20] = r[20] + 1
	beq	r20	r11	loop1	#r[3] == r[2] keep going
	nop
	j	loop			# goto loop
	nop
	ld	r20	0	r0
loop1	dadd	r2	r2	r2
	daddi	r20	r20	1
	beq	r20	r11	loop2
	nop
	j	loop1
	nop
	ld	r20	0	r0
loop2	dadd	r3	r3	r3
	daddi	r20	r20	1
	beq	r20	r11	loop3
	nop
	j	loop2
	nop
	ld	r20	0	r0
loop3	dadd	r4	r4	r4
	daddi	r20	r20	1
	beq	r20	r11	loop4
	nop
	j	loop3
	nop
	ld	r20	0	r0
loop4	dadd	r5	r5	r5
	daddi	r20	r20	1
	beq	r20	r11	loop5
	nop
	j	loop4
	nop
	ld	r20	0	r0
loop5	dadd	r6	r6	r6
	daddi	r20	r20	1
	beq	r20	r11	loop6
	nop
	j	loop5
	nop
	ld	r20	0	r0
loop6	dadd	r7	r7	r7
	daddi	r20	r20	1
	beq	r20	r11	loop7
	nop
	j	loop6
	nop
	ld	r20	0	r0
loop7	dadd	r8	r8	r8
	daddi	r20	r20	1
	beq	r20	r11	loop8
	nop
	j	loop7
	nop
	ld	r20	0	r0
loop8	dadd	r9	r9	r9
	daddi	r20	r20	1
	beq	r20	r11	end
	nop
	j	loop8
	nop
end	halt
zero	.dfill	0
one	.dfill	1
two	.dfill	2
three	.dfill	3
four	.dfill	4
five	.dfill	5
six	.dfill	6
seven	.dfill	7
eight	.dfill	8
nine	.dfill	9
ten	.dfill	10
