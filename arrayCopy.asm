      daddi r1 r0 20
      daddi r2 r0 0
loop  ld r3 array1 r2
      sd r3 array2 r2
      daddi r2 r2 8
      daddi r1 r1 -1
      bne r0 r1 loop
      halt
array1  .dfill 1
        .dfill 2
        .dfill 3
        .dfill 4
        .dfill 5
        .dfill 6
        .dfill 7
        .dfill 8
        .dfill 9
        .dfill 10
        .dfill 11
        .dfill 12
        .dfill 13
        .dfill 14
        .dfill 15
        .dfill 16
        .dfill 17
        .dfill 18
        .dfill 19
        .dfill 20
array2  .dfill -1
        .dfill -1
        .dfill -1
        .dfill -1
        .dfill -1
