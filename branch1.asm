       beq r0 r1 target
       dump 1
target dump 2              # should only see dump of GPRs
       halt
