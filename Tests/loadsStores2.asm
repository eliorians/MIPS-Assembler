        l.d f0 here    r0   # 0  load0 here is 38
        s.d f0 store1 r0    # 4  store0 store1 is 50
        ld r1 there r0      # 8  load1 there is 40
        ld r2 more r0       # c  load2 more is 48
        sd r1 store2 r0     # 10 store1 store2 is 58
        sd r2 store3 r0     # 14 store2 store3 is 60
        ld r3 addr r0       # 18 load3 addr is 68
        ld r4 0   r3        # 1c load0 A set to 0 until load3 done
        sd r4 fourtn2 r0    # 20
        ld r5 three r0      # 24
        sd r5 three2 r0     # 28
        halt                # 30
here   .dfill 3.7           # 38
there  .dfill 2             # 40
more   .dfill 15            # 48
store1 .dfill 0             # 50
store2 .dfill 0             # 58
store3 .dfill 0             # 60
addr   .dfill fourtn        # 68
fourtn   .dfill 14          # 70
fourtn2  .dfill 0           # 78
three  .dfill 3             # 80
three2 .dfill 0             # 88
