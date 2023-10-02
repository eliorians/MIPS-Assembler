#office hours 3-5 T/R

import sys
import os

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
    #find byte location of all labels and store them somewhere to be referred to?
        #labels do not have a space infront of them

    #while not empty
    #track pc counter
    #if statement for every instruction type

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