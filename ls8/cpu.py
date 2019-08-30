"""CPU functionality."""

import sys


ADD = 10100000 
SUB = 10100001 
MUL = 10100010 
DIV = 10100011 
MOD = 10100100
CMP = 10100111
AND = 10101000
LDI = 10000010
LD = 10000011
OR  = 10101010
XOR = 10101011
SHL = 10101100
SHR = 10101101
ST = 10000100
#NOP = 00000000
#INC = 0110010
#DEC = 01100110
#PRN = 01000111
#PRA = 01001000
#N0T = 01101001
# JMP = 01010100
# JNE = 01010110
# JLT = 01011000
# JGT = 01010111
# JGE = 01011010
# JEQ = 01010101
# HLT = 00000001

ADD = '10100000' 
SUB = '10100001' 
MUL = '10100010' 
DIV = '10100011' 
MOD = '10100100'
CMP = '10100111'
AND = '10101000'
LDI = '10000010'
LD  = '10000011'
OR  = '10101010'
XOR = '10101011'
SHL = '10101100'
SHR = '10101101'
ST  = '10000100'
NOP = '00000000'
INC = '0110010'
DEC = '01100110'
PRN = '01000111'
PRA = '01001000'
NOT = '01101001'
JMP = '01010100'
JNE = '01010110'
JLT = '01011000'
JGT = '01010111'
JGE = '01011010'
JEQ = '01010101'
HLT = '00000001'

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} filename")
    sys.exit(1)
try: 
    initial_memory = [0] * 256
    counter = 0
    with open(sys.argv[1]) as f:
        for line in f:
            #print(line.split('#', 1))
            num = line.split('#', 1)[0]
            num = num.split('\n', 1)[0]
            print(num, type(num))
            initial_memory[counter] = num
            counter += 1


except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.agrv[1]} not found.")
    sys.exit(2)





#print(ADD, SUB, MUL)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = initial_memory
        self.registers = [0] * 8
        self.program_counter = 0
        self.instruction_register = 0
        self.stack_pointer = 0xF4
        #self.memory[0] = 10100000  # ADD
        self.flags = 11111000 # 00000LGE L = Less than , G = Greater than, E = Equal



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
        # for line in self.memory:
        #     print(line)
    # 0 - Have all this in a loop
        running = True

        while(running):
            if type(self.ram_read(self.program_counter)) == int:
                break
        # 1 - Have instructions loaded to memory

        # 2 - call the proper instruction

            self.instruction_register = self.ram_read(self.program_counter)
            print("Instruction: ", self.instruction_register, type(self.instruction_register), HLT, type(HLT))
            if int(self.instruction_register, 2) == int(HLT, 2):
                print("In halt, PC =  ", self.program_counter)
                return 0
                
            operand_1 = int(self.ram_read(self.program_counter + 1), 2)
            operand_2 = int(self.ram_read(self.program_counter + 2), 2)
            print("operand_1 : ", operand_1, type(operand_1), self.program_counter)
            
            val1 = self.registers[operand_1]
            if operand_2 < 8:
                val2 = self.registers[operand_2]



            if int(self.instruction_register, 2) == int(ADD, 2):
                self.registers[operand_1] = val1 + val2
                
            elif int(self.instruction_register, 2) == int(SUB, 2):
                self.registers[operand_1] = val1 - val2
                
            elif int(self.instruction_register, 2) == int(MUL, 2):
                self.registers[operand_1] = val1 * val2
                
            elif int(self.instruction_register, 2) == int(DIV, 2):
                self.registers[operand_1] = val1 / val2
                
            elif int(self.instruction_register, 2) == int(MOD, 2):
                self.registers[operand_1] = val1 % val2

            elif int(self.instruction_register, 2) == int(NOT, 2):
                self.registers[operand_1] = ~ val1 

            elif int(self.instruction_register, 2) == int(INC, 2):
                self.registers[operand_1] = val1 + 1

            elif int(self.instruction_register, 2) == int(DEC, 2):
                self.registers[operand_1] = val1 - 1
                
            elif int(self.instruction_register, 2) == int(CMP, 2):
                
                if val1 == val2:
                    self.flags = '11111001'
                # TODO: set equal flag to 1 if equal, to zero otherwise
                elif val1 < val2:
                    self.flags = '11111100'
                # TODO: set less than flag to 1 if equal, to zero otherwise
                else:
                    self.flags = '11111010'
                # TODO: set greater than flag to 1 if equal, to zero otherwise

            elif int(self.instruction_register, 2) == int(AND, 2):
                self.register[operand_1] = val1 & val2

            elif int(self.instruction_register, 2) == int(OR, 2):
                self.register[operand_1] = val1 | val2

            elif int(self.instruction_register, 2) == int(XOR, 2):
                self.register[operand_1] = val1 ^ val2

            elif int(self.instruction_register, 2) == int(SHL, 2):
                self.register[operand_1] = val1 << val2

            elif int(self.instruction_register, 2) == int(SHR, 2):
                self.register[operand_1] = val1 >> val2

            elif int(self.instruction_register, 2) == int(ST, 2):
                self.memory[val1] = val2

            elif int(self.instruction_register, 2) == int(PRN, 2):
                print("in print value")
                print(val1)

            elif int(self.instruction_register, 2) == int(PRA, 2):
                print(str(chr(val1)))

            elif int(self.instruction_register, 2) == int(NOP, 2):
                pass

            elif int(self.instruction_register, 2) == int(LDI, 2):
                self.registers[operand_1] = operand_2

            elif int(self.instruction_register, 2) == int(LDI, 2):
                self.registers[operand_1] = self.memory[val1]

            elif int(self.instruction_register, 2) == int(JMP, 2):
                self.program_counter = val1
                continue

            elif int(self.instruction_register, 2) == int(JNE, 2):
                flags = self.flags
                flags = int(str(flags), 2) & int('00000001', 2)
                if flags == 0:
                    self.program_counter = val1
                    continue

            elif int(self.instruction_register, 2) == int(JLT, 2):
                flags = self.flags
                flags = int(str(flags), 2) & int('00000100', 2)
                if flags == 100:
                    self.program_counter = val1
                    continue

            elif int(self.instruction_register, 2) == int(JGT, 2):
                flags = self.flags
                flags = int(str(flags), 2) & int('00000010', 2)
                if flags == 10:
                    self.program_counter = val1
                    continue

            elif int(self.instruction_register, 2) == int(JGE, 2):
                flags = self.flags
                flags = int(str(flags), 2) & int('00000011', 2)
                if flags == 10 or flags == 1:
                    self.program_counter = val1
                    continue

            elif int(self.instruction_register, 2) == int(JEQ, 2):
                flags = self.flags
                flags = int(str(flags), 2) & int('00000001', 2)
                if flags == 1:
                    self.program_counter = val1
                    continue

            

            num_of_operands = int(str(self.instruction_register), 2) >> 6

            self.program_counter += num_of_operands + 1







prog = CPU()
prog.run()