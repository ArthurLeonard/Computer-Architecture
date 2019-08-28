"""CPU functionality."""

import sys


ADD = 10100000 
SUB = 10100001 
MUL = 10100010 
DIV = 10100011 
MOD = 10100100
#INCC = 0110010
#DEC = 01100110
CMP = 10100111
AND = 10101000
#NOT = 01101001 
OR  = 10101010
XOR = 10101011
SHL = 10101100
SHR = 10101101

print(ADD, SUB, MUL)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = [0] * 256
        self.registers = [0] * 8
        self.program_counter = 0
        self.instruction_register = 0
        self.stack_pointer = 0xF4


    def ram_read(self, address):
        return self.memory[address]

    def ram_write(self, address, value):
        self.memory[address] = value


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
    # 0 - Have all this in a loop

        # 1 - Have instructions loaded to memory

        # 2 - call the proper instruction

        self.instruction_register = self.ram_read(program_counter)
        operand_1 = self.ram_read(program_counter + 1)
        operand_2 = self.ram_read(program_counter + 2)

        if self.instruction_register == ADD:
            self.registers[operand_1] = self.registers[operand_1] + self.registers[operand_2]
            
        elif self.instruction_register == SUB:
            self.registers[operand_1] = self.registers[operand_1] - self.registers[operand_2]
            
        elif self.instruction_register == MUL:
            self.registers[operand_1] = self.registers[operand_1] * self.registers[operand_2]
            
        elif self.instruction_register == DIV:
            self.registers[operand_1] = self.registers[operand_1] / self.registers[operand_2]
            
        elif self.instruction_register == MOD:
            self.registers[operand_1] = self.registers[operand_1] % self.registers[operand_2]
            
        elif self.instruction_register == CMP:
            pass
        elif self.instruction_register == AND:
            pass

        elif self.instruction_register == OR:
            pass

        elif self.instruction_register == XOR:
            pass

        elif self.instruction_register == SHL: 
            pass

        elif self.instruction_register == SHR:
            pass
