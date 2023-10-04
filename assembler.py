#office hours 3-5 T/R

import sys
import os

#list of possible registers
registers = [f'r{i}' for i in range(32)]

def register_to_binary(register_str):
        # Extract the numeric part from the input string
        register_num = int(register_str[1:])
    
        # Check if the register number is within the valid range (0 to 31)
        if 0 <= register_num <= 31:
            # Convert the register number to 5-bit binary and return it as a string
            binary_representation = format(register_num, '05b')
            return binary_representation
        else:
            return "Invalid register number"
        
def label_to_binary(label, label_dict):
    byte = label_dict[label]
    decimal_byte = int(byte)
    # Convert to binary, removing the '0b' prefix
    binary_byte = bin(decimal_byte)[2:]  
    # Ensure the binary string is 16 bits long, filling with leading zeros if necessary
    return binary_byte.zfill(16)  

def remove_label(line, label):
    words = line.split()
    if label in words:
        words.remove(label)
    return ' '.join(words)

def binary_to_hex(binary_str):
    hex_str = hex(int(binary_str, 2)) 
    # Remove the '0x' prefix and return the result
    return hex_str[2:].zfill(8)

def decimal_to_binary16(decimal_str):
    decimal_num = int(decimal_str)
    # Convert to binary and remove '0b' prefix
    binary_str = bin(decimal_num)[2:]  
    # Pad with leading zeros to make it 16 bits long
    binary_str = binary_str.zfill(16)
    return binary_str

def decimal_to_binary26(decimal_str):
    decimal_num = int(decimal_str)
    # Convert to binary and remove '0b' prefix
    binary_str = bin(decimal_num)[2:]  
    # Pad with leading zeros to make it 26 bits long
    binary_str = binary_str.zfill(26)
    return binary_str

def main():
    #get file and put each line into a string in list
    inputFile = sys.argv[1]
    lines = open(inputFile).read().splitlines()

    #remove lone comments and empty lines
    for i in lines[:]:
        if len(i)==0:         
            lines.remove(i)
        if i.startswith('#'): 
            lines.remove(i)
    
    #remove comments from inside lines    
    for i in range(len(lines)):
        if '#' in lines[i]:
            lines[i] = lines[i].split('#')[0]

    #label calculation
    byte = 0
    labels = {}
    for i in range(len(lines)):
        #find byte location of all labels and store as dict to be refered to later
        j = lines[i]
        if j[0].isalpha():
            l = j.split()[0]
            labels[l] = byte
            #remove the label
            lines[i] = remove_label(lines[i], l)
        
        #increment byte, if line contains .dfill, byte+8
        if '.dfill' in lines[i]:
            byte = byte+8
        else:
            byte = byte+4

    #remove leading & trailing spaces
    for i in range(len(lines)):
        lines[i] = lines[i].strip()    
    
    #convert instructions to binary
    pc = 0
    offset = 0
    binary = []
    comments = []
    invalid = False
    for i in range(len(lines)):
        line = lines[i]
        comments.append(' # '+remove_label(line, labels))
        line = line.split()
        binaryLine = ""

        #! operation (instruction type)
        #! fields incoming
        #! encoding

        #ld (I) from label
        #Opcode 55 in 6 bits / rt in 5 bits / imm in 16 bits (from labels) / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        if (line[0]=='ld' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '110111'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)
            #ld from immm
        elif (line[0]=='ld' and line[1] in registers and line[2].isdigit() and line[3] in registers):
            binaryLine = '110111'+register_to_binary(line[3])+register_to_binary(line[1])+decimal_to_binary16(line[2])
            binary.append(binaryLine)

        #l.d (I)
        #Opcode 53 in 6 bits / rt in 5 bits / imm in 16 bits (from labels) / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='l.d' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '110101'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)
            
            
        #TODO sd (I)
        #
        #

        #TODO s.d (I)
        #
        #

        #daddi (I) immediate
        #Opcode 24 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (decimal# -> binary)
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='daddi' and line[1] in registers and line[2] in registers and line[3].isdigit()):
            binaryLine = '011000'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(line[3])
            binary.append(binaryLine)
        #daddu label
        elif (line[0]=='daddi' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '011000'+register_to_binary(line[2])+register_to_binary(line[1])+label_to_binary(line[3], labels)
            binary.append(binaryLine)

        #daddiu (I)
        #Opcode 25 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (decimal# -> binary)
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='daddiu' and line[1] in registers and line[2] in registers and line[3].isdigit()):
            binaryLine = '011001'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(line[3])
            binary.append(binaryLine)

        #beq (I) label
        # Opcode 4 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (abs(pc - label)/8)
        # encoding: opcode / rs / rt / imm
        elif (line[0]=='beq' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '000100'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(abs((pc-int(labels[line[3]]))/8))
            binary.append(binaryLine)
        #beq imm
        elif (line[0]=='beq' and line[1] in registers and line[2] in registers and line[3].isdigit):
            binaryLine = '000100'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(int(line[3]))
            binary.append(binaryLine)
        #bne (I)
        # Opcode 5 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (abs(pc - label)/8)
        # encoding: opcode / rs / rt / imm
        elif (line[0]=='bne' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '000101'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(abs((pc-int(labels[line[3]]))/8))
            binary.append(binaryLine)

        #dadd (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 46 in 6 bits
        elif (line[0]=='dadd' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'101100'
            binary.append(binaryLine)

        #TODO dsub (R)
        #
        #

        #TODO add.d (R)
        #
        #

        #TODO sub.d (R)
        #
        #

        #TODO mul.d (R)
        #
        #

        #TODO div.d (R)
        #
        #

        #j (J) label
        # OpCode 2 in 6 bits / offset 26 bits
        # opcode / offset
        elif (line[0]=='j' and line[1] in labels):
            binaryLine = '000010'+decimal_to_binary26(labels[line[1]]/4)
            binary.append(binaryLine)
        #j imm
        elif (line[0]=='j' and line[1].isdigit()):
            binaryLine = '000010'+decimal_to_binary26(line[1])
            binary.append(binaryLine)

        #halt (J)
        # OpCode 1 in 6 bits / offset 26 bits
        # opcode / offset
        elif (line[0]=='halt'):
            binaryLine = '000001'+decimal_to_binary26(0)
            binary.append(binaryLine)

        #nop (J)
        # OpCode 3 in 6 bits / offset 26 bits
        # opcode / offset
        elif (line[0]=='nop'):
            binaryLine = '000011'+decimal_to_binary26(0)
            binary.append(binaryLine)

        #TODO dump (J)
        #
        #

        #.dfil
        # store data into two lines, add no comment line
        elif (line[0]=='.dfill'):
            binaryLine = bin(int(line[1]))[2:].zfill(32)
            binaryLeft = binaryLine[:16]
            binaryRight = binaryLine[16:]
            binary.append(binaryRight)
            binary.append(binaryLeft)
            comments.append('')

        #not valid
        else:
            print("Invalid input on line " + str(offset))
            print(lines[i])
            invalid = True
            break

        #increment pc counter, if line contains .dfill, byte+8
        if '.dfill' in lines[i]:
            pc = pc+8
            offset = offset+2
        else:
            pc = pc+4
            offset = offset+1

    #convert binary to hex
    hex = []
    for i in range(len(binary)):
        hex.append(binary_to_hex(binary[i]))
                
    #write to output file, places line then newline
    outputFile = os.path.splitext(inputFile)[0]+'.hex'
    output = open(outputFile, 'w')
    for i in range(len(hex)):
        #only write file if valid input
        output.writelines(hex[i] + comments[i] + '\n')
        print(hex[i] + comments[i])
    #removes last new line
    #output.truncate(output.tell()-len(os.linesep))
    output.close()

if __name__ == "__main__":
    main()