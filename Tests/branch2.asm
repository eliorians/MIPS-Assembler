       bne r0 r1 target
       dump 2              # should see this dump (GPRs)
       j done
target dump 1              # should not see this dump 
done   halt
