    l.d f0 num1a r0
    l.d f1 num2a r0
    div.d f2 f0 f1
    s.d f2 resulta r0
#
    l.d f0 num1b r0
    l.d f1 num2b r0
    div.d f2 f0 f1
    s.d f2 resultb r0
#
    l.d f0 num1c r0
    l.d f1 num2c r0
    div.d f2 f0 f1
    s.d f2 resultc r0
#
    l.d f0 num1d r0
    l.d f1 num2d r0
    div.d f2 f0 f1
    s.d f2 resultd r0
#
    l.d f0 num1e r0
    l.d f1 num2e r0
    div.d f2 f0 f1
    s.d f2 resulte r0
#
    l.d f0 num1f r0
    l.d f1 num2f r0
    div.d f2 f0 f1
    s.d f2 resultf r0
#
    halt
num1a .dfill 2.0
num1b .dfill 4.0
num1c .dfill 8.0
num1d .dfill 16.0
num1e .dfill 24.0
num1f .dfill 36.0
num2a .dfill 1.0
num2b .dfill 2.0
num2c .dfill 4.0
num2d .dfill 8.0
num2e .dfill 3.0
num2f .dfill 6.0
resulta .dfill 0
resultb .dfill 0
resultc .dfill 0
resultd .dfill 0
resulte .dfill 0
resultf .dfill 0
