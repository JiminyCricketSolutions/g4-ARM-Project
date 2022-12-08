#### ARMassemble
## NAME: Zack Deal
## CLASS: CPE-221-01
## DATE(S): 11/24/22 - 12/7/22
## DESCRIPTION: Takes an ARM file and makes
##  an output file where the ARM is translated to Binary.
## COMMENTS/CONCERNS: Converts to LogicArrays that are then exported
##      to a .txt file for importation by another handling python
##      program.
## LIST:
##  11/24/22 - Unsure how to use cocotb's LogicArrays. Relearning file manipulation with Python.
##          Nothing major achieved.
##  11/27/22 - Program no longer compiling. Found and installed miniconda and cocotb. Experimenting
##          with LogicArrays when outputing to files and how to manipulate them.
##  11/28/22 - Still confused. Python is an interesting langauge. Nothing major accomplished.
##  11/29/22 - Gave group simple ARM code in binary for testing on the processor while Assembler is being
##          completed.
##  12/1/22 - Assembler still not complete. Received help. No longer trying to implement CMP, PUSH, or POP.
##  12/3/22 - Given ARM code had a mistake. Fixed. Now attempting to assemble given ARM code, not fibonnaci programs.
##  12/4/22 - Program now compiles. MOV, ADD, SUB, ORR, and AND implemented.
##  12/6/22 - STR, LDR, and BRANCH now implemented. Nearly done. 80%. Maybe.
##  12/7/22 - Assembler is in a semi-working state. Ready to be tested on the processor. Binary
##          does not match up exactly, but may still execute the same program. Branching may be
##          handled incorrectly - unsure. Back to working on the Final.
##  12/7/22 (FINAL) - Uploaded to Git at 9:30 PM. Uploaded with the input and output files.
##
##  HOW TO USE: Run the program once in terminal. After that, call the assemble function with the designated
##      file. Will work with .s or .txt files, up to you. Once run, it will output the binary both to terminal
##      (at least for PYTHON) but also to the file Machine_RAW.txt. This .txt file should be loaded into the
##      ARMMEMLOADER.py - check that program for instructions on how to modify and run that.
####

## Imports
import sys
import re
import cocotb
from cocotb.types import LogicArray, Range

## Should allow the program to be run outside of the file - i.e. via terminal
def assemble(file):
    mach_bin = []
    branches = {}
    labels = {}

    def check_branch(file_input):                                                           ## Part of BRANCH
        address = 0
        
        with open(file_input) as f:
            
            for line in f:
                line = line.replace('\n', '').replace('\r', '').replace('\t', '')
                bit = re.split(r'[, ]',line)
                
                if (bit[0].lower() == "b") or (bit[0].lower() == "bl") or (bit[0].lower() == "beq") or (bit[0].lower() == "bge"):
                    branches[bit[1]] = address
            
                if line[0]=='.':
                    labels[line[1:]] = address
            
                else:
                    address = address + 1 

    check_branch(file)

    with open(file) as f:
        
        for line in f:
            
            if line[0]=='.':
                continue
            
            line = line.replace('\n', '').replace('\r', '').replace('\t', '')
            bit = re.split(r'[, ]',line)
        
            while '' in bit:
                bit.remove('')
            
            if not bit:
                continue
        
            if bit[0].lower() == "mov":                                                     ## MOV
            
                if bit[1].lower() == "pc":
                    rd = LogicArray(15, Range(3, "downto", 0))
                else:
                    rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[2]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("1110000110100000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:16] = b0
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
            	
                elif src2 == 'lr':
            	    rm = LogicArray(14, Range(11, "downto", 0))
            	    b0 = LogicArray("1110000110100000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:16] = b0
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
            	
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("1110001110100000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:16] = b0
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
        	
            elif bit[0].lower() == "add":                                                   ## ADD
        
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[3]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000001000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000101000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
            elif bit[0].lower() == "addlt":
        
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[3]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("101100001000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("101100101000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
        
            elif bit[0].lower() == "sub":                                                   ## SUB
            
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[3]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000000100")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000100100")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
            elif bit[0].lower() == "subs":
            
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[3]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000000101")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000100101")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
        
            elif bit[0].lower() == "and":                                                   ## AND
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[3]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000000000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000100000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
        
            elif bit[0].lower() == "orr":                                                   ## ORR
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].lower()[1:]), Range(3, "downto", 0))
            
                src2 = bit[3]
                if src2[0].lower() == 'r':
            	    rm = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000011000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = rm
            	    
            	    mach_bin.append(bin_final)
                else:
            	    v = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
            	    b0 = LogicArray("111000111000")
            	    bin_final = LogicArray(0, Range(31, "downto", 0))
            	    bin_final[31:20] = b0
            	    bin_final[19:16] = rn
            	    bin_final[15:12] = rd
            	    bin_final[11:0] = v
            	    
            	    mach_bin.append(bin_final)
        
            elif bit[0].lower() == "str":                                                   ## STR
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].replace('[', '')[1:]), Range(3, "downto", 0))
            
                src2 = bit[3].replace(']', '')
                if src2[0].lower() == 'r':
                    rm = LogicArray(int(src2[1:], 0), Range(3, "downto", 0))
                    b0 = LogicArray("111001111000")
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:20] = b0
                    bin_final[19:16] = rn
                    bin_final[15:12] = rd
                    bin_final[11:4] = "00000001"
                    bin_final[3:0] = rm
                    
                    mach_bin.append(bin_final)
                else:
                    imm12 = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
                    b0 = LogicArray("111001011000")
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:20] = b0
                    bin_final[19:16] = rn
                    bin_final[15:12] = rd
                    bin_final[11:0] = imm12
                    
                    mach_bin.append(bin_final)
                
            elif bit[0].lower() == "ldr":                                                   ## LDR
                rd = LogicArray(int(bit[1].lower()[1:]), Range(3, "downto", 0))
                rn = LogicArray(int(bit[2].replace('[', '')[1:]), Range(3, "downto", 0))
            
                src2 = bit[3].replace(']', '')
                if src2[0].lower() == 'r':
                    rm = LogicArray(int(src2[1:], 0), Range(3, "downto", 0))
                    b0 = LogicArray("111001111001")
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:20] = b0
                    bin_final[19:16] = rn
                    bin_final[15:12] = rd
                    bin_final[11:4] = "00000001"
                    bin_final[3:0] = rm
                    
                    mach_bin.append(bin_final)
                else:
                    imm12 = LogicArray(int(src2[1:], 0), Range(11, "downto", 0))
                    b0 = LogicArray("111001011001")
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:20] = b0
                    bin_final[19:16] = rn
                    bin_final[15:12] = rd
                    bin_final[11:0] = imm12
                    
                    mach_bin.append(bin_final)
        
            elif bit[0].lower() == "b":                                                     ## BRANCH
                if bit[1] in labels:
                    addr = labels[bit[1]]
                    v = addr - (branches[bit[1]] + 2)
                    imm24 = LogicArray(v, Range(23, "downto", 0))
                    b0 = "11101010"
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:24] = b0
                    bin_final[23:0] = imm24
                    
                    mach_bin.append(bin_final)
            elif bit[0].lower() == "beq":
                if bit[1] in labels:
                    addr = labels[bit[1]]
                    v = addr - (branches[bit[1]] + 2)
                    imm24 = LogicArray(v, Range(23, "downto", 0))
                    b0 = "00001010"
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:24] = b0
                    bin_final[23:0] = imm24
                    
                    mach_bin.append(bin_final)
            elif bit[0].lower() == "bge":
                if bit[1] in labels:
                    addr = labels[bit[1]]
                    v = addr - (branches[bit[1]] + 2)
                    imm24 = LogicArray(v, Range(23, "downto", 0))
                    b0 = "10101010"
                    bin_final = LogicArray(0, Range(31, "downto", 0))
                    bin_final[31:24] = b0
                    bin_final[23:0] = imm24
                    
                    mach_bin.append(bin_final)


    with open("Machine_RAW.txt", "w") as output:                                            ## OUTPUT TO FILE
        for item in mach_bin:
            output.write(item.binstr) 
            output.write("\n")
    output.close()
    
    return mach_bin
