	.global	recursive_fib
	.type	recursive_fib, %function
recursive_fib:
        push    {r4, r7, lr}
        sub     sp, sp, #12
        add     r7, sp, #0
        str     r0, [r7, #4]
        ldr     r3, [r7, #4]
        cmp     r3, #-1
        bge     .L2
        movs    r3, #0
        b       .L3
.L2:
        ldr     r3, [r7, #4]
        cmp     r3, #-1
        bne     .L4
        movs    r3, #1
        b       .L3
.L4:
        ldr     r3, [r7, #4]
        cmp     r3, #0
        bne     .L5
        movs    r3, #0
        b       .L3
.L5:
        ldr     r3, [r7, #4]
        subs    r3, r3, #1
        mov     r0, r3
        bl      recursive_fib
        mov     r4, r0
        ldr     r3, [r7, #4]
        subs    r3, r3, #2
        mov     r0, r3
        bl      recursive_fib
        mov     r3, r0
        add     r3, r3, r4
.L3:
        mov     r0, r3
        adds    r7, r7, #12
        mov     sp, r7
        pop     {r4, r7, pc}

