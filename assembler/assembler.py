register_table = {
    "x0": "00000",
    "x1": "00001",
    "x2": "00010",
    "x3": "00011",
    "x4": "00100",
    "x5": "00101",
    "x6": "00110",
    "x7": "00111",
    "x8": "01000",
    "x9": "01001",
    "x10": "01010",
    "x11": "01011",
    "x12": "01100",
    "x13": "01101",
    "x14": "01110",
    "x15": "01111",
    "x16": "10000",
    "x17": "10001",
    "x18": "10010",
    "x19": "10011",
    "x20": "10100",
    "x21": "10101",
    "x22": "10110",
    "x23": "10111",
    "x24": "11000",
    "x25": "11001",
    "x26": "11010",
    "x27": "11011",
    "x28": "11100",
    "x29": "11101",
    "x30": "11110",
    "x31": "11111",
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "fp": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111",
}

csr_table = {
    "sstatus": 256,  # 0x100
    "sie": 260,  # 0x104
    "stvec": 261,  # 0x105
    "scounteren": 262,  # 0x106
    "scounterinhibit": 288,  # 0x120
    "sscratch": 320,  # 0x140
    "sepc": 321,  # 0x141
    "scause": 322,  # 0x142
    "stval": 323,  # 0x143
    "sip": 324,  # 0x144
    "satp": 384,  # 0x180
    "cycle": 3072,  # 0xC00
    "time": 3073,  # 0xC01
    "instret": 3074,  # 0xC02
    "stimecmp": 333,  # 0x14D
    "senvcfg": 266,
}

opcode_table = {
    "lui": "0110111",
    "auipc": "0010111",
    "jal": "1101111",
    "jalr": "1100111",
    "beq": "1100011",
    "bne": "1100011",
    "blt": "1100011",
    "bge": "1100011",
    "bltu": "1100011",
    "bgeu": "1100011",
    "lb": "0000011",
    "lh": "0000011",
    "lw": "0000011",
    "lbu": "0000011",
    "lhu": "0000011",
    "addi": "0010011",
    "andi": "0010011",
    "ori": "0010011",
    "xori": "0010011",
    "slti": "0010011",
    "sltiu": "0010011",
    "slli": "0010011",
    "srli": "0010011",
    "srai": "0010011",
    "add": "0110011",
    "sub": "0110011",
    "sll": "0110011",
    "slt": "0110011",
    "sltu": "0110011",
    "xor": "0110011",
    "srl": "0110011",
    "sra": "0110011",
    "or": "0110011",
    "and": "0110011",
    "csrrw": "1110011",
    "csrrs": "1110011",
    "csrrc": "1110011",
    "csrrwi": "1110011",
    "csrrsi": "1110011",
    "csrrci": "1110011",
    "ecall": "1110011",
    "sret": "1110011",
    "sw": "0100011",
    "sb": "0100011",
    "sh": "0100011",
}

funct3_table = {
    "add": "000",
    "sub": "000",
    "addi": "000",
    "sb": "000",
    "lb": "000",
    "beq": "000",
    "jalr": "000",
    "ecall": "000",
    "sret": "000",
    "sll": "001",
    "slli": "001",
    "sh": "001",
    "lh": "001",
    "bne": "001",
    "csrrw": "001",
    "slt": "010",
    "slti": "010",
    "sw": "010",
    "lw": "010",
    "csrrs": "010",
    "sltu": "011",
    "sltiu": "011",
    "csrrc": "011",
    "xor": "100",
    "xori": "100",
    "lbu": "100",
    "blt": "100",
    "srl": "101",
    "sra": "101",
    "srli": "101",
    "srai": "101",
    "lhu": "101",
    "bge": "101",
    "csrrwi": "101",
    "or": "110",
    "ori": "110",
    "bltu": "110",
    "csrrsi": "110",
    "and": "111",
    "andi": "111",
    "bgeu": "111",
    "csrrci": "111"
}

funct7_table = {
    "sra": "0100000",
    "srai": "0100000",
    "sub": "0100000",
    "slli": "0000000",
    "srl": "0000000",
    "add": "0000000",
    "sll": "0000000",
    "slt": "0000000",
    "sltu": "0000000",
    "xor": "0000000",
    "or": "0000000",
    "and": "0000000",
    "srli": "0000000",
    "sret": "0001000",
}

r_type = ["add", "sub", "and", "or", "xor", "sll", "srl", "slt", "sltu", "sra"]
i_type = ["addi", "andi", "ori", "xori", "slti", "sltiu"]
shilf_i = ["slli", "srli", "srai"]
load = ["lb", "lh", "lw", "lbu", "lhu", "jalr"]
store = ["sb", "sh", "sw"]
b_type = ["beq", "bne", "blt", "bge", "bltu", "bgeu"]
u_type = ["lui", "auipc"]
j_type = ["jal"]
system = ["csrrw", "csrrs", "csrrc"]
systemi = ["csrrwi", "csrrsi", "csrrci"]
sret = ["sret"]
ecall = ["ecall"]
la = ["la"]

def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.

    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    with open(file_path, "r") as file:
        content = file.read()
    return content


def write_file(file_path, content):
    """
    Writes the given content to a file.

    :param file_path: Path to the file where content will be written.
    :param content: Content to write to the file.
    """
    with open(file_path, "w") as file:
        file.write(content)

def format_assembly_instruction(instruction):
    
    pass

def assembler(instructions):
    """
    Converts an assembly instruction to machine code.

    :param instruction: Assembly instruction as a string.
    :return: Machine code as a string.
    """
    # This function should implement the logic to convert the assembly instruction
    # into machine code using the opcode_table, funct3_table, funct7_table, etc.
    # For now, it returns a placeholder value.
    machine_code = "00000000000000000000000000000000"  # Placeholder for machine code
    return machine_code


def run_direct(input_file_path, output_folder_path, index):
    pass
    
    
def run_all(input_folder_path, output_folder_path, num_files):
    """
    Main function to run the assembler.

    :param file_path: Path to the assembly file to be assembled.
    """
    for i in range(num_files):
        input_file_path = f"{input_folder_path}/assembly_file_{i}.asm"
        output_file_path_bin = f"{output_folder_path}/machine_code_file_{i}.bin"
        output_file_path_hex = f"{output_folder_path}/machine_code_file_{i}.bin"
        run_direct(input_file_path, output_file_path, i)