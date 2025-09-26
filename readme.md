Simple Computer Architecture Simulator
This project is a Python-based simulation of a basic computer architecture. It includes several key components that work together to execute a program, from low-level logical gates to a high-level operating system.

The simulator demonstrates the fundamental relationships between different parts of a computer system, such as the CPU, memory, and storage, and how assembly code is translated into machine code and executed.

Core Components Explained
The project is structured into several modules, each representing a different part of the simulated computer.

File

Deeper Explanation

processing_unit.py

This file simulates the Central Processing Unit (CPU), which acts as the brain of the entire system. It is responsible for orchestrating every operation. The core functionality is within its run() method, which initiates the execution cycle. Inside this cycle, the CPU uses a program counter to keep track of the current instruction's address. It fetches an instruction, decodes it using the decode() function, and then executes it by calling the appropriate methods on other components like the ALU, RAM, and storage devices.

operating_system.py

This isn't a full-fledged operating system, but rather the main program code for the simulation, written in the project's custom assembly language. It acts as the "OS" by defining the sequence of operations the CPU should perform. This includes setting up system calls to interact with hardware and defining application logic.

assembler.py & dissamble.py

These two files handle the critical process of translating between human-readable code and machine-executable code. The assembler takes the assembly instructions from operating_system.py and converts them into binary machine code that the CPU can understand. The disassembler performs the reverse process, taking binary code and translating it back into assembly. This is an essential tool for debugging and understanding the low-level program flow.

arthmetic_logic_unit.py

The Arithmetic Logic Unit (ALU) is a component of the CPU that performs all mathematical and logical operations. It contains methods for standard arithmetic like ADD, SUB, MUL, and DIV, as well as more complex bitwise operations like AND, OR, XOR, SHL (shift left), and SHR (shift right). The ALU also handles conditional logic and comparisons, which are essential for instructions like COND_JUMP.

random_accsess_memory.py

This module simulates Random Access Memory (RAM). It is a form of volatile storage that the CPU uses for quick access to data and instructions. The simulated RAM has a limited capacity of 256 addresses, each capable of storing an 8-bit binary value. The CPU constantly reads from and writes to RAM during program execution.

HEAP.py

The Heap simulates a section of memory used for dynamic data allocation. While similar to RAM, it serves a specialized purpose for managing data structures and values that are created or destroyed during a program's runtime. The simulated Heap has 256 addresses, each capable of holding a large 84-bit value.

harddrive.py & SSD_CARD.py

These modules simulate two different types of non-volatile storage: a Hard Disk Drive and a Solid State Drive. They are used for long-term storage of programs and files. The CPU loads the machine code from these devices into its internal components for execution. The hard drive has a capacity of 1000 addresses, while the SSD card has a much larger capacity of over 65,000 addresses.

moniter.py

The Monitor serves as the simple visual output for the simulation. It takes binary data representing an image and renders it as a text-based display. It translates each '1' bit into a \# character and each '0' bit into a space, allowing for a basic representation of on-screen graphics.

Instruction Set Architecture (ISA) Deep Dive
The simulator uses a custom instruction set, where each instruction is represented by a binary opcode. Here is a more detailed breakdown of the key opcodes and their functions:

1000 (ARTH): This is the opcode for all arithmetic and logical operations. It is followed by a sub-opcode that tells the ALU exactly what to do. The sub-opcode can range from 001000 for ADD to 011001 for LT (less than). This design allows a single instruction type to perform a wide variety of functions.

1010 (SYS_CALL): This instruction switches the CPU to "kernel mode" to perform a system-level operation. This is how the program interacts with hardware, such as creating a file on the hard drive or displaying output on the monitor.

1011 (APP_CALL): This instruction switches the CPU back to "user mode" to continue executing the main application code after a system call has completed.

0111 (WRITE_RAM): The CPU uses this command to write a new value to a specified address in the RAM.

0101 (READ_RAM): This command allows the CPU to fetch and read the data stored at a specific address in the RAM.

1100 (WRITE_HEAP): This is used to write data to the dynamic memory section simulated by the Heap.

1101 (MOVE_H_HD): This is a key data transfer instruction. It moves a value from a specified address in the Heap to a specified address on the hard drive.

0001 (JUMP): This instruction performs an unconditional jump, changing the value of the program counter to a new address. This is used for creating loops or skipping sections of code.

0010 (COND_JUMP): This instruction performs a conditional jump. It checks a specific condition (e.g., if a value is zero) before deciding whether to jump to a new address.

11111111 (HALT): This is the final instruction that terminates all CPU operations, bringing the program to a graceful end.

1010001000 (CREATE_FILE): This is an example of a specific system call that the CPU can execute to create a new file on a storage device.

The Program Workflow
The process of running a program in this simulation follows a clear sequence:

Assembly: The operating_system.py file, which contains a series of assembly instructions, is passed to the assembler.py module.

Machine Code Generation: The assembler translates each assembly instruction into a corresponding binary machine code command. For example, a command like WRITE_HEAP becomes a binary string like 1100 followed by the address and data.

Loading: The resulting binary machine code is then loaded into the harddrive.py or SSD_CARD.py modules, where it is stored for execution.

Execution: The processing_unit.py file starts its run() method. The CPU's program counter is initialized to the starting address of the program on the hard drive.

Fetch-Decode-Execute Cycle:

Fetch: The CPU fetches the instruction from the current address specified by the program counter.

Decode: The decode() function interprets the binary opcode to determine what action to perform.

Execute: The CPU performs the required action, which could involve using the ALU for a calculation, writing to RAM or HEAP, or sending data to the moniter.

Next Instruction: After execution, the CPU increments the program counter to move to the next instruction in the sequence. This cycle repeats until the HALT instruction is encountered.

This entire process provides a comprehensive, albeit simplified, view of how a computer's hardware and software interact to run a program.