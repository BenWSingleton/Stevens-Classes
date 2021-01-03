/*
 * taylor.s
 *
 *  Created on: Dec 9, 2020
 *      Author: Benjamin Singleton
 *      Pledge: I pledge my honor that I have abided by the Stevens Honor System.
 */
  .text
  .global main
  .extern printf

main:
  .global taylor_main


taylor_main:
  LDR x1, =initial
  LDR d1, [x1] //d1 keeps track of the approximation, starting at 1.0
  LDR x3, =i
  LDR x2, [x3] //x2 keeps track of how many terms are wanted in the approximation
  mov x19, #1  //x19 keeps track of what nth term we're on.
  LDR x4, =x
  LDR d3, [x4] //loads x into d3 to be copied as necessary
  bl loop
taylor_main_end:
  br x30

  .func loop
loop:
  CMP x2, #1 //check if the counter is down to 1
  beq end
  ORR x20, xzr, xzr //counter for exp function
  ADD x20, x19, xzr
  fmov d5, d3
exp:
  cmp x20, #1
  beq exp_end
  fmul d5, d3, d5
  sub x20, x20, #1
  b exp
exp_end:
  fadd d1, d1, d5
  add x19, x19, #1
  sub x2, x2, #1
  b loop
end:
  fmov d0, d1
  LDR x0, =prt_str1
  bl printf
  br x30
  .endfunc



  .data
i: //number of terms in the approximation
  .quad 6
initial: //initial value for the approximation
  .double 1.0
x: //value of x
  .double 2.3
zero:
  .double 0.0
prt_str1:
  .ascii "The approximation is %f\n\0"
   .end

