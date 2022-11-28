	.global	iterative_fib
	.type	iterative_fib, %function
iterative_fib:
        push    {r7}
        sub     sp, sp, #28
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
        movs    r3, #1
        str     r3, [r7, #20]
        movs    r3, #0
        str     r3, [r7, #16]
        movs    r3, #0
        str     r3, [r7, #8]
        movs    r3, #1
        str     r3, [r7, #12]
        b       .L6
.L7:
        ldr     r3, [r7, #20]
        str     r3, [r7, #8]
        ldr     r2, [r7, #20]
        ldr     r3, [r7, #16]
        add     r3, r3, r2
        str     r3, [r7, #20]
        ldr     r3, [r7, #8]
        str     r3, [r7, #16]
        ldr     r3, [r7, #12]
        adds    r3, r3, #1
        str     r3, [r7, #12]
.L6:
        ldr     r2, [r7, #12]
        ldr     r3, [r7, #4]
        cmp     r2, r3
        blt     .L7
        ldr     r3, [r7, #20]
.L3:
        mov     r0, r3
        adds    r7, r7, #28
        mov     sp, r7
        ldr     r7, [sp], #4
        bx      lr

