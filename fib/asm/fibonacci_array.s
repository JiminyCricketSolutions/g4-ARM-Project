	.global	fibonacci_array
	.type	fibonacci_array, %function
fibonacci_array:
        push    {r4, r7, lr}
        sub     sp, sp, #28
        add     r7, sp, #0
        str     r0, [r7, #12]
        str     r1, [r7, #8]
        str     r2, [r7, #4]
        movs    r3, #0
        str     r3, [r7, #20]
        b       .L9
        
.L10:
        ldr     r2, [r7, #4]
        ldr     r3, [r7, #20]
        adds    r1, r2, r3
        ldr     r3, [r7, #20]
        lsls    r3, r3, #2
        ldr     r2, [r7, #12]
        adds    r4, r2, r3
        mov     r0, r1
        bl      recursive_fib
        mov     r3, r0
        str     r3, [r4]
        ldr     r3, [r7, #20]
        adds    r3, r3, #1
        str     r3, [r7, #20]
        
.L9:
        ldr     r2, [r7, #20]
        ldr     r3, [r7, #8]
        cmp     r2, r3
        blt     .L10
        adds    r7, r7, #28
        mov     sp, r7
        pop     {r4, r7, pc}
