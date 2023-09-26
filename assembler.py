
import sys
import os

def main():

    #get file and put each line into a string in list
    inputFile = sys.argv[1]
    lines = open(inputFile).read().splitlines()

    


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