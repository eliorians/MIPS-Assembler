import os
import sys
import struct

#Office Hours:
#Monday 11-3
#Tuesday 3-5

testing = False
#cd /u/css/classes/5483/111/MA/

def binary_to_hex(binary_str):
    hex_str = hex(int(binary_str, 2)) 
    # Remove the '0x' prefix and return the result
    return hex_str[2:].zfill(8)

#list of possible registers
registers = []
for i in range(32):
    registers.append(f"r{i}")
    registers.append(f"f{i}")

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

def decimal_to_binary16(decimal_number):
    if decimal_number >= 0:
        # Convert positive decimal to binary
        binary_representation = bin(int(decimal_number))[2:].zfill(16)
    else:
        # Convert negative decimal to binary using two's complement
        positive_binary = bin(int(abs(decimal_number)))[2:].zfill(16)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
        carry = 1
        binary_representation = ''
        
        for bit in reversed(inverted_binary):
            if bit == '0' and carry == 1:
                binary_representation = '1' + binary_representation
                carry = 0
            elif bit == '1' and carry == 1:
                binary_representation = '0' + binary_representation
            else:
                binary_representation = bit + binary_representation
    
    return binary_representation

def decimal_to_binary26(decimal_str):
    decimal_num = int(decimal_str)
    #convert to binary and remove '0b' prefix
    binary_str = bin(decimal_num)[2:]  
    #pad with leading zeros to make it 26 bits long
    binary_str = binary_str.zfill(26)
    return binary_str
    
def decimal_to_binary32(decimal_number):
    if decimal_number >= 0:
        # Convert positive decimal to binary
        binary_representation = bin(int(decimal_number))[2:].zfill(32)
    else:
        # Convert negative decimal to binary using two's complement
        positive_binary = bin(int(abs(decimal_number)))[2:].zfill(32)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
        carry = 1
        binary_representation = ''
        
        for bit in reversed(inverted_binary):
            if bit == '0' and carry == 1:
                binary_representation = '1' + binary_representation
                carry = 0
            elif bit == '1' and carry == 1:
                binary_representation = '0' + binary_representation
            else:
                binary_representation = bit + binary_representation
    
    return binary_representation

def float_to_binary32(num):
    # Pack the decimal number into a binary representation using struct.pack
    # with the 'd' format, which represents a double-precision float.
    packed = struct.pack('d', num)
    # Unpack the binary representation and convert it to a binary string.
    # Use bin() to convert the unpacked value to a binary string.
    binary_string = bin(struct.unpack('<Q', packed)[0])[2:]
    # Pad the binary string with leading zeros to ensure it has 64 bits.
    padded_binary_string = binary_string.zfill(64)
    return padded_binary_string

def label_to_binary32(label, label_dict):
    byte = label_dict[label]
    decimal_byte = int(byte)
    # Convert to binary, removing the '0b' prefix
    binary_byte = bin(decimal_byte)[2:]  
    # Ensure the binary string is 16 bits long, filling with leading zeros if necessary
    return binary_byte.zfill(32)  

def extend_binary32(binary_str, is_negative):
    if is_negative:
        binary_str = '1' * (32 - len(binary_str)) + binary_str
    else:
        binary_str = '0' * (32 - len(binary_str)) + binary_str
    
    return binary_str

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def remove_label(line, label):
    words = line.split()
    if label in words:
        words.remove(label)
    return ' '.join(words)

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
        
        #if halt ends on byte not a multiple of 8 then padd with 0's to make it so
        if 'halt' in lines[i] and byte % 8 != 0:
            byte = byte + 4

    #remove leading & trailing spaces
    for i in range(len(lines)):
        lines[i] = lines[i].strip()    
    #convert instructions to binary
    pc = 0
    offset = 0
    binary = []
    comments = []
    for i in range(len(lines)):
        line = lines[i]
        comments.append(' # ' + line)
        line = line.split()
        binaryLine = ""

        #operation (instruction type)
        #fields incoming
        #encoding
        
        #ld (I) from label
        #Opcode 55 in 6 bits / rt in 5 bits / imm in 16 bits (from labels) / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        if (line[0]=='ld' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '110111'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)
            #ld from immm
        elif (line[0]=='ld' and line[1] in registers and line[2].isdigit() and line[3] in registers):
            binaryLine = '110111'+register_to_binary(line[3])+register_to_binary(line[1])+decimal_to_binary16(int(line[2]))
            binary.append(binaryLine)

        #l.d (I) from lable
        #Opcode 53 in 6 bits / rt in 5 bits / imm in 16 bits (from labels) / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='l.d' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '110101'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)
            #l.d from imm
        elif (line[0]=='l.d' and line[1] in registers and line[2].isdigit() and line[3] in registers):
            binaryLine = '110101'+register_to_binary(line[3])+register_to_binary(line[1])+decimal_to_binary16(int(line[2]))
            binary.append(binaryLine)
            
        #sd (I) from labels
        #Opcode 63 in 6 bits / rt in 5 bits / imm in 16 bits (from labels) / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='sd' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '111111'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)
            #sd from immm
        elif (line[0]=='sd' and line[1] in registers and line[2].isdigit() and line[3] in registers):
            binaryLine = '111111'+register_to_binary(line[3])+register_to_binary(line[1])+decimal_to_binary16(int(line[2]))
            binary.append(binaryLine)

        #s.d (I) from labels
        #Opcode 61 in 6 bits / rt in 5 bits / imm in 16 bits (from labels) / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='s.d' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '111101'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)
            #sd from immm
        elif (line[0]=='s.d' and line[1] in registers and line[2].isdigit() and line[3] in registers):
            binaryLine = '111101'+register_to_binary(line[3])+register_to_binary(line[1])+decimal_to_binary16(int(line[2]))
            binary.append(binaryLine)

        #daddi (I) from immediate
        #Opcode 24 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (decimal# -> binary)
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='daddi' and line[1] in registers and line[2] in registers and is_integer(line[3])):
            binaryLine = '011000'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(int(line[3]))
            binary.append(binaryLine)
            #daddi from label
        elif (line[0]=='daddi' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '011000'+register_to_binary(line[2])+register_to_binary(line[1])+label_to_binary(line[3], labels)
            binary.append(binaryLine)

        #daddiu (I) from imm
        #Opcode 25 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (decimal# -> binary)
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='daddiu' and line[1] in registers and line[2] in registers and is_integer(line[3])):
            binaryLine = '011001'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(int(line[3]))
            binary.append(binaryLine)
            #daddiu from label
        elif (line[0]=='daddiu' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '011001'+register_to_binary(line[2])+register_to_binary(line[1])+label_to_binary(line[3], labels)
            binary.append(binaryLine)

        #beq (I) label
        # Opcode 4 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (target - pc+4) // 4)
        # encoding: opcode / rs / rt / imm
        elif (line[0]=='beq' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '000100'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16((int(labels[line[3]]) - (pc+4)) // 4)
            binary.append(binaryLine)
            #beq imm
        elif (line[0]=='beq' and line[1] in registers and line[2] in registers and line[3].isdigit):
            binaryLine = '000100'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(int(line[3]))
            binary.append(binaryLine)

        #bne (I) from label
        # Opcode 5 in 6 bits / rt in 5 bits / rs in 5 bits / imm in 16 bits (target - pc+4) // 4)
        # encoding: opcode / rs / rt / imm
        elif (line[0]=='bne' and line[1] in registers and line[2] in registers and line[3] in labels):
            binaryLine = '000101'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16((int(labels[line[3]]) - (pc+4)) // 4)
            binary.append(binaryLine)
            #bne from imm
        elif (line[0]=='bne' and line[1] in registers and line[2] in registers and line[3].isdigit):
            binaryLine = '000101'+register_to_binary(line[2])+register_to_binary(line[1])+decimal_to_binary16(int(line[3]))
            binary.append(binaryLine)

        #dadd (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 44 in 6 bits
        elif (line[0]=='dadd' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'101100'
            binary.append(binaryLine)

        #dsub (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 46 in 6 bits
        elif (line[0]=='dsub' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'101110'
            binary.append(binaryLine)

        #add.d (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 47 in 6 bits
        elif (line[0]=='add.d' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'101111'
            binary.append(binaryLine)

        #sub.d (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 48 in 6 bits
        elif (line[0]=='sub.d' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'110000'
            binary.append(binaryLine)

        #mul.d (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 49 in 6 bits
        elif (line[0]=='mul.d' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'110001'
            binary.append(binaryLine)

        #div.d (R)
        # OpCode 0 in 6 bits / rd in 5 bits / rs in 5 bits / rt in 5 bits
        # opcode / rs / rt / rd / shamt (0) in 5 bits / funct 50 in 6 bits
        elif (line[0]=='div.d' and line[1] in registers and line[2] in registers and line[3] in registers):
            binaryLine = '000000'+register_to_binary(line[2])+register_to_binary(line[3])+register_to_binary(line[1])+'00000'+'110010'
            binary.append(binaryLine)

        #j (J) label
        # OpCode 2 in 6 bits / offset 26 bits
        # opcode / offset
        elif (line[0]=='j' and line[1] in labels):
            binaryLine = '000010'+decimal_to_binary26(int(labels[line[1]]/4))
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
            #if halt doesnt end on multiple of 8, make it so (but only if there are lines after!)
            if ((pc+4) % 8 != 0 and lines[i] != lines[-1]):
                binaryLine = decimal_to_binary32(0)
                binary.append(binaryLine)
                comments.append('')

        #nop (J)
        # OpCode 3 in 6 bits / offset 26 bits
        # opcode / offset
        elif (line[0]=='nop'):
            binaryLine = '000011'+decimal_to_binary26(0)
            binary.append(binaryLine)

        #dump (J)
        # OpCode 44 in 6 bits / data in 26 bits
        # opcode / offset
        elif (line[0]=='dump' and line[1].isdigit()):
            binaryLine = '101100'+decimal_to_binary26(line[1])
            binary.append(binaryLine)

        #.dfil for decimals + or -
        # store data into two lines, add no comment line
        elif (line[0]=='.dfill' and is_integer(line[1])):
            binaryLine = decimal_to_binary32(int(line[1]))
            
            binaryLeft = binaryLine[:16]
            binaryRight = binaryLine[16:]
            #if number was negative, fill out the remaining 1's
            is_neg = False
            if (int(line[1]) < 0):
                is_neg = True
            binaryLeft = extend_binary32(binaryLeft, is_neg)
            binaryRight = extend_binary32(binaryRight, is_neg)
            binary.append(binaryRight)
            binary.append(binaryLeft)
            comments.append('')

        #todo .dfil for floats + or -, currently is wrong
        # store data into two lines, add no comment line
        elif (line[0]=='.dfill' and is_float(line[1])):
            binaryLine = float_to_binary32(float(line[1]))
            print(binaryLine)
            binaryLeft = binaryLine[:32]
            binaryRight = binaryLine[32:]
            binary.append(binaryRight)
            binary.append(binaryLeft)
            comments.append('')

        #.dfil for labels
        # store data into two lines, add no comment line
        elif (line[0]=='.dfill' and line[1] in labels):
            binaryLine = label_to_binary32(line[1], labels)
            binaryLeft = binaryLine[:16]
            binaryRight = binaryLine[16:]
            binary.append(binaryRight)
            binary.append(binaryLeft)
            comments.append('')
        
        #not valid
        else:
            print("Invalid input on line " + str(offset))
            print(lines[i])
            #print all the stuff if in testing mode
            if(testing):
                break
            else:
                exit()

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
    if (testing):
        print('...')
    outputFile = os.path.splitext(inputFile)[0]+'.hex'
    output = open(outputFile, 'w')
    for i in range(len(hex)):
        output.writelines(hex[i] + comments[i] + '\n')
        if(testing):
            print(hex[i] + comments[i])
    output.close()

if __name__ == "__main__":
    main()