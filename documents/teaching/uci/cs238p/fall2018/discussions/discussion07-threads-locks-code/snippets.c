/* 
The following code is not executable. It consists of snippets 
with line numbers extracted from the xv6 source print at 
https://pdos.csail.mit.edu/6.828/2018/xv6/xv6-rev11.pdf, and from 
http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf
This file has been saved as a .c file for pedagogical purposes - to obtain
colored code formatting when opened in a C syntax recognizing IDE/editor. 
*/

// -------- POSIX thread creation ----------- //

// page 4 - http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf

// The following uses POSIX (Portable Operating System Interface)
// thread API to create threads.
1 #include <stdio.h>
2 #include <assert.h>
3 #include <pthread.h>
4
5 void *mythread(void *arg) {
6 printf("%s\n", (char *) arg);
7 return NULL;
8 }
9
10 int
11 main(int argc, char *argv[]) {
12 pthread_t p1, p2;
13 int rc;
14 printf("main: begin\n");

// main thread creates thread p1 
15 rc = pthread_create(&p1, NULL, mythread, "A"); assert(rc == 0);

// main thread creates thread p2 
16 rc = pthread_create(&p2, NULL, mythread, "B"); assert(rc == 0);

17 // join waits for the threads to finish
18 rc = pthread_join(p1, NULL); //main thread waits for p1
   assert(rc == 0);
19 rc = pthread_join(p2, NULL); //main thread waits for p2
   assert(rc == 0);
20 printf("main: end\n");
21 return 0;
22 }

// -------- A spin-lock data structure ----------- //

// Xv6 represents a spin-lock as a struct spinlock. 

//  xv6/spinlock.h 
1501 struct spinlock {
1502 uint locked; // Is the lock held? (0 - it is available; 1 - it is not)
1503
1504 // For debugging:
1505 char *name; // Name of lock.
1506 struct cpu *cpu; // The cpu holding the lock.
1507 uint pcs[10]; // The call stack (an array of program counters)
1508 // that locked the lock.
1509 };

// -------- A spin-lock implementation that doesn't work ----------- //

// page 54 - https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf
21 void
22 acquire(struct spinlock *lk)
23 {
24 for(;;) { // the spinning part

// 2 different CPUs may reach the line below and see that the lock is available, 
// and therefore, acquire the lock --- creating a race condition of its own.
25 	if(!lk->locked) {	//--------> | Need these two instructions 
26 		lk->locked = 1; //--------> | to execute atomically (i.e., in one go)
27 		break;
28 	}
29 }
30 }


// -------- The correct spin-lock in xv6 ----------- //

// xv6/x86.h
0569 xchg(volatile uint *addr, uint newval)
0570 {
0571 uint result;
0572

	 // The following is an assembly block.
	 // "Making an inline asm block "volatile" ... ensures that, as it optimizes, 
	 // the compiler does not move any instructions above or below the block of asm statements."
	 // "In any asm block, assembly instructions appear first, followed by 
	 // the inputs and outputs, which are separated by a colon."
0573 // The + in "+m" denotes a read−modify−write operand.
0574 asm volatile("lock; xchgl %0, %1" :
0575 "+m" (*addr), "=a" (result) :
0576 "1" (newval) :
0577 "cc");
0578 return result;
0579 }

// xv6/spinlock.c
1569 // Acquire the lock.
1570 // Loops (spins) until the lock is acquired.
1571 // Holding a lock for a long time may cause
1572 // other CPUs to waste time spinning to acquire it.
1573 void
1574 acquire(struct spinlock *lk)
1575 {
1576 	pushcli(); // disable interrupts to avoid deadlock.
// "Without interruption, a thread can be sure that the code it executes will execute
// and that no other thread will interfere with it." [2]

1577 	if(holding(lk))
1578 	panic("acquire");
1579
1580 	// The xchg is atomic. 
1581 	while(xchg(&lk−>locked, 1) != 0) //xchg returns &lk->locked
1582 	;
		// Note that spinning can be inefficient.
1583
1584 	// Tell the C compiler and the processor to not move loads or stores
1585 	// past this point, to ensure that the critical section’s memory
1586 	// references happen after the lock is acquired.
1587	 __sync_synchronize();
1588
1589 	// Record info about lock acquisition for debugging. In case a thread fails.
1590 	lk−>cpu = mycpu();
1591 	getcallerpcs(&lk, lk−>pcs);
1592 }

Commentary References:
[1] https://www.ibm.com/developerworks/rational/library/inline-assembly-c-cpp-guide/index.html
[2] http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf