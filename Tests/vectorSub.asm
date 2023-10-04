# vector loop - calculates Y[i] = X[i] - Y[i]
#
        daddi  r1 r0  X    # initialize r1 to X
        daddi  r2 r0  Y    # initialize r2 to Y
        daddi  r3 r0  10   # initialize r3 to 10 
        daddi  r4 r0  0    # initialize r4 to 0
foo     l.d f2 0 r1        # load X[i]
        l.d f6 0 r2        # load Y[i]
        sub.d f6 f2 f6     # add X[i] - Y[i]
        s.d  f6 0 r2       # store Y[i]
        daddiu r1 r1 8     # increment X index
        daddiu r2 r2 8     # increment Y index
        daddiu r4 r4 1     # r4 = r4 + 1
        bne r4 r3 foo      # branch if r4 != 10 
        halt
X       .dfill 1.1
        .dfill 2.2
        .dfill 3.3
        .dfill 4.4
        .dfill 5.5
        .dfill 6.6
        .dfill 7.7
        .dfill 8.8
        .dfill 9.9
        .dfill 10.10
Y       .dfill 1.0
        .dfill 2.0
        .dfill 3.0
        .dfill 4.0
        .dfill 5.0
        .dfill 6.0
        .dfill 7.0
        .dfill 8.0
        .dfill 9.0
        .dfill 10.0
