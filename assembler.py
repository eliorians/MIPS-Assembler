#office hours 3-5 T/R
import sys
import os

#list of possible registers

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
    binary_byte = bin(decimal_byte)[2:]  # Convert to binary, removing the '0b' prefix
    return binary_byte.zfill(16)  # Ensure the binary string is 16 bits long, filling with leading zeros if necessary

def binary_to_hex(binary_str):
    
    hex_str = hex(int(binary_str, 2)).upper()  
    # Remove the '0x' prefix and return the result
    return hex_str[2:]

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
            l = j.split(" ")[0]
            labels[l] = byte
        
        #increment byte, if line contains .dfill, byte+8
        if '.dfill' in lines[i]:
            byte = byte+8
        else:
            byte = byte+4
    
    #create list of possible registers
    registers = [f'r{i}' for i in range(32)]

    #convert to binary
    pc = 0
    offset = 0
    binary = []
    for i in range(len(lines)):
        line = lines[i]
        line = line.split()
        binaryLine = ""

        #ld operation 
        #Opcode 55 in 6 bits / rt in 5 bits / imm in 16 bits / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        if (line[0]=='ld' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '110111'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)

        #l.d operation
        #Opcode 53 in 6 bits / rt in 5 bits / imm in 16 bits / rs in 5 bits / 
        #encoding: opcode / rs / rt / imm
        elif (line[0]=='l.d' and line[1] in registers and line[2] in labels and line[3] in registers):
            binaryLine = '110101'+register_to_binary(line[3])+register_to_binary(line[1])+label_to_binary(line[2],labels)
            binary.append(binaryLine)

        #not a valid line
        else:
            print("Invalid input on line "+str(offset))
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
                
    print(hex)

    #write to output file, places line then newline
    outputFile = os.path.splitext(inputFile)[0]+'.hex'
    output = open(outputFile, 'w')
    for i in lines:
        output.writelines(i + '\n')
    #removes last new line
    output.truncate(output.tell()-len(os.linesep))
    output.close()

if __name__ == "__main__":
    main()