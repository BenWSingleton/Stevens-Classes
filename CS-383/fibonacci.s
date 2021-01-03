/*
 * fibonacci.s
 *
 *  Created on: Oct 29, 2020
 *      Author: Benjamin Singleton
 *     Version: 2
 *      Pledge: I pledge my honor that I have abided by the Stevens Honor System.
 */

  .equ input, 12      //nth fibonacci number
  .text
  .global main
  .extern printfs

main:
  .global fib_main

fib_main:
  ldr x0, =string
  mov x3, input       //n
  mov x2, #0          //fibprevious
  mov x1, #1          //fibcurrent
  bl fib
fib_main_end:
  br x30

  .func fib
fib:
  cmp x3, #1          //Does n==1
  bhi L1
  b fib_end

L1:
  sub x3, x3, #1      //n=n-1
  ORR x19, XZR, XZR   //temp register
  add x19, XZR, x1    //store fibCurrent in temp
  add x1, x2, x1      //fibCurrent=fibCurrent+fibPrevious
  ORR x2, XZR, XZR    //empty fibPrevious
  add x2, x19, XZR    //fibPrevious = temp
  bl fib

fib_end:
  bl printf
  br x30
  .endfunc
  .data

string:
  .ascii "%d\n\0"
  .end
