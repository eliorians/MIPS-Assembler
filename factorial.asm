# this program computes the factorial of 8 numbers
         daddi r1 r0 num1          # address of first number
         daddi r2 r0 fact1         # address of first result
         daddi r3 r0 0             # counter register
         daddi r4 r0 8             # number of factorials to compute
         ld  r7 two r0             # set r7 to 2
loop     ld r5 0 r1                # num1 = fact
         ld r6 0 r1                # i = fact
         dadd  r9 r0 r5            # result to fact (for 2!)
inner    beq r6 r7 cont            # if i = 2 continue
         dadd  r9 r0 r0            # result to 0
         daddi r10 r6 -1           # num2 = i - 1
in2      beq r10 r0 break          # if (num2 == 0) exit inner loop
         dadd r9 r9 r5             # result = result + num1
         daddi r10 r10 -1          # num2 = num2 - 1
         j in2
break    dadd r5 r0 r9             # num1 = result
         daddi r6 r6 -1            # i = i - 1
         j inner
cont     sd r9 0 r2                # store result
         daddi r1 r1 16            # get next fact address
         daddi r2 r2 16            # get next result address
         daddi r3 r3 1
         bne r3 r4 loop
         halt
two      .dfill 2
num1     .dfill 2
fact1    .dfill 0
num2     .dfill 4
fact2    .dfill 0
num3     .dfill 3
fact3    .dfill 0
num4     .dfill 5
fact4    .dfill 0
num5     .dfill 8
fact5    .dfill 0
num6     .dfill 10
fact6    .dfill 0
num7     .dfill 15
fact7    .dfill 0
num8     .dfill 7
fact8    .dfill 0
