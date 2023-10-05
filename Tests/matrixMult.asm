          daddiu r1 r0 a00      # r1 is starting address of a00
          daddiu r2 r0 b00      # r2 is starting address of b00
          daddiu r3 r0 c00      # r7 is starting address of c00
          ld r4 esize r0        # r4 is size of elements (8)
          ld r5 arowno r0       # r5 is number of rows of a
          ld r6 bcolno r0       # r6 is number of cols of b
          ld r7 acolno r0       # r7 is number of cols of a
          ld r8 arowsize r0     # r8 is number of bytes in a row of a
          ld r9 browsize r0     # r9 is number of bytes in a row of b
          daddi r10 r0 0        # init m to 0
          daddi r11 r0 0        # init n to 0
Out       beq r11 r5 done       
          dadd r12 r1 r10       # aptr = a + m
          daddi r13 r0 0        # k = 0
          daddi r14 r0 0        # i = 0
Mid       beq r13 r6 doneMid
          daddi r15 r12 0       # another aptr = aptr
          dadd r16 r2 r14       # bptr = b + i
          l.d f0 zero r0        # result = 0.0
          daddi r18 r0 0        # j = 0
In        beq r18 r7 doneIn
          l.d f1 0 r15          # get a element
          l.d f2 0 r16          # get b element
          mul.d f1 f2 f1      
          add.d f0 f0 f1        # result += a element * b element
          dadd r15 r15 r4       # another aptr += element size
          dadd r16 r16 r9       # bptr += browsize
          daddi r18 r18 1       # j++ 
          j In 
doneIn    s.d f0 0 r3          # store result in c
          dadd r3 r3 r4        # increment c address by element size
          dadd r14 r14 r4      # i = i + elementsize
          daddi r13 r13 1      # k++
          j Mid 
doneMid   dadd r10 r10 r8      # m = m + arowsize
          daddi r11 r11 1      # n++
          j Out 
done      halt
esize    .dfill 8
acolno   .dfill 3
arowno   .dfill 2
arowsize .dfill 24
bcolno   .dfill 2
browsize .dfill 16
zero     .dfill 0.0
a00      .dfill 1.0
a01      .dfill 2.0
a02      .dfill 3.0
a10      .dfill 2.0
a11      .dfill 3.0
a12      .dfill 4.0
b00      .dfill 1.0
b01      .dfill 2.0
b10      .dfill 2.0
b11      .dfill 3.0
b20      .dfill 3.0
b21      .dfill 4.0
c00      .dfill 0
c01      .dfill 0
c10      .dfill 0
c11      .dfill 0
