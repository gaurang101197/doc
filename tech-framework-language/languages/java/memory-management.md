# JVM memory management

Memory management is the process of allocating new objects and removing
unused objects to make space for those new object allocations.

## Stack memory

Each Java Virtual Machine thread has a private *Java Virtual Machine stack*, created at the same time as the thread.

- If the computation in a thread requires a larger Java Virtual Machine stack than is permitted, the Java Virtual Machine throws a `StackOverflowError`.
- If Java Virtual Machine stacks can be dynamically expanded, and expansion is attempted but insufficient memory can be made available to effect the expansion, or if insufficient memory can be made available to create the initial Java Virtual Machine stack for a new thread, the Java Virtual Machine throws an `OutOfMemoryError`.

### What does it store ?

It holds local variables and partial results, and plays a part in method invocation and return.

### **Stack Frame**

- A *frame* is used to store data and partial results, as well as to perform dynamic linking, return values for methods, and dispatch exceptions.
- A new frame is created each time a method is invoked. A frame is destroyed when its method invocation completes, whether that completion is normal or abrupt (it throws an uncaught exception).
- A frame ceases to be current if its method invokes another method or if its method completes. When a method is invoked, a new frame is created and becomes current when control transfers to the new method. On method return, the current frame passes back the result of its method invocation, if any, to the previous frame. The current frame is then discarded as the previous frame becomes the current one.

Each frame contains:

- [Local Variable Array (LVA)](https://docs.oracle.com/javase/specs/jvms/se11/html/jvms-2.html#jvms-2.6.1)
  - The Java Virtual Machine uses local variables to pass parameters on method invocation. On **class** method invocation, any parameters are passed in consecutive local variables starting from local variable *0*. On **instance** method invocation, local variable *0* is always used to pass a reference to the object on which the instance method is being invoked (`this` in the Java programming language). Any parameters are subsequently passed in consecutive local variables starting from local variable *1.*
  - A single local variable can hold a value of type `boolean`, `byte`, `char`, `short`, `int`, `float`, `reference`, or `returnAddress`. A pair of local variables can hold a value of type `long` or `double`.
- [Operand Stack (OS](https://docs.oracle.com/javase/specs/jvms/se11/html/jvms-2.html#jvms-2.6.2))
  - Each frame contains a last-in-first-out (LIFO) stack known as its *operand stack*. The operand stack is empty when the frame that contains it is created. The Java Virtual Machine supplies instructions to load constants or values from local variables or fields onto the operand stack. Other Java Virtual Machine instructions take operands from the operand stack, operate on them, and push the result back onto the operand stack. The operand stack is also used to prepare parameters to be passed to methods and to receive method results.
  - For example, the *iadd* instruction ([§*iadd*](https://docs.oracle.com/javase/specs/jvms/se11/html/jvms-6.html#jvms-6.5.iadd)) adds two `int` values together. It requires that the `int` values to be added be the top two values of the operand stack, pushed there by previous instructions. Both of the `int` values are popped from the operand stack. They are added, and their sum is pushed back onto the operand stack. Subcomputations may be nested on the operand stack, resulting in values that can be used by the encompassing computation.
  - Each entry on the operand stack can hold a value of any Java Virtual Machine type, including a value of type `long` or type `double`.

## On-Heap memory

The Java Virtual Machine has a *heap* that is shared among all Java Virtual Machine threads. The heap is the run-time data area from which memory for all **class instances and arrays** is allocated.

- The heap is created on virtual machine start-up. Heap storage for objects is reclaimed by an automatic storage management system (known as a ***garbage collecto**r*); objects are never explicitly deallocated. The Java Virtual Machine assumes no particular type of automatic storage management system, and the storage management technique may be chosen according to the implementor's system requirements. The heap may be of a fixed size or may be expanded as required by the computation and may be contracted if a larger heap becomes unnecessary. The memory for the heap does not need to be contiguous.
- A Java Virtual Machine implementation may provide the programmer or the user control over the initial size of the heap, as well as, if the heap can be dynamically expanded or contracted, control over the maximum and minimum heap size.
- If a computation requires more heap than can be made available, the Java Virtual Machine throws an `OutOfMemoryError`.

The heap is sometimes divided into two areas (or *generations*) called

1. the *nursery* (or *young space*) and
2. the *old space*.

The nursery is a part of the heap reserved for allocation of new objects. When the nursery becomes full, garbage is collected by running a special *young collection*, where all objects that have lived long enough in the nursery are *promoted* (moved) to the old space, thus freeing up the nursery for more object allocation. When the old space becomes full garbage is collected there, a process called an *old collection*.

### Why we have different generations in heap ?

The reasoning behind it is that most objects are temporary and short lived. A young collection is designed to be swift at finding newly allocated objects that are still alive and moving them away from the nursery. Typically, a young collection frees a given amount of memory much faster than an old collection or a garbage collection of a single-generational heap (a heap without a nursery).

### References

1. <https://docs.oracle.com/javase/specs/jvms/se11/html/jvms-2.html>
2. <https://docs.oracle.com/javase/specs/jvms/se11/html/jvms-2.html#jvms-2.5.3>
3. <https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html>
