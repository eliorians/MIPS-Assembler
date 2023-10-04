#add two arrays and store results
	daddi	r1	r0	first	# 		r1 = 	addr of a[0]
	daddi	r2	r0	second	#r2 = addr of b[0]
	daddi	r3	r0	4	#r3 = 4
	daddi	r7	r0	8	#r7 = 8
	daddi	r8	r0	sum	#write results here
loop	ld	r4	0	r1	# r4 = a[first + i]
	ld	r5	0	r2	# r5 = b[second + i]
	dadd	r6	r4	r5	#r6 = a[i] + b[i]
	sd	r6	0	r8	#store results
	daddi	r1	r1	4	#r1 += 4
	daddi	r2	r2	4	#r2 += 4
	dadd	r4	r4	r3	#r4 += 4
	dadd	r5	r5	r3	#rt += 4
	dadd	r8	r8	r7	# step to next place to store
	beq	r4	r2	end	# a's pointer has reached b so stop
	nop
	j	loop
	nop
end	halt
first	.dfill	1
	.dfill	2
	.dfill	3
	.dfill	4
	.dfill	5
	.dfill	6
	.dfill	7
	.dfill	8
	.dfill	9
	.dfill	10
	.dfill	11
	.dfill	12
	.dfill	13
	.dfill	14
	.dfill	15
	.dfill	16
	.dfill	17
	.dfill	18
	.dfill	19
	.dfill	20
second	.dfill	1
	.dfill	2
	.dfill	3
	.dfill	4
	.dfill	5
	.dfill	6
	.dfill	7
	.dfill	8
	.dfill	9
	.dfill	10
	.dfill	11
	.dfill	12
	.dfill	13
	.dfill	14
	.dfill	15
	.dfill	16
	.dfill	17
	.dfill	18
	.dfill	19
	.dfill	20
sum	.dfill	0
