# This module is used to load code from a file into the memory of the
# Processor

# By Elijah Moore

# To use this in the toplevel module, one must simply take note



class program:
    """
    Anticipated purpose is to use this to load program into processor
    expected syntax for this after importing this module is

    prog = program("File Name")
    prog.gotoStart()
    while not prog.atEnd:
        #   _________________ The part below the underscores may need to change to our specific design.
        dut.datapath.imem.mem[prog.programLine].setimmediatevalue(LogicArray(prog.getNextInstruction()).integer)


    """


    def __init__(self, MachineCodeFileName):
        file = open(MachineCodeFileName, 'r')   # Opens file in Text Mode
        self.program = file.readlines()         # to change to binary mode,
        file.close()                            # Set 'r' to 'r+b'
                                                
        self.programLength = len(self.program)
        # print(f"Program Length is {self.programLength}")
        self.programLine = 0

        self._updateFlags()

        

    def getNextInstruction(self):
        
        #if it would be out of range, reset to 0
        if self.programLine >= self.programLength:
            self.programLine = 0

        # We get the 32 bit instructions, clean out the spaces
        instruction = self.program[self.programLine].strip()

        # Increment line of program
        self.programLine += 1
        
        # Update el flago
        self._updateFlags()
        
        # Send out instruction as a string.
        return instruction

    def _updateFlags(self):
        if self.programLine == 0:
            self.atStart = True
        else:
            self.atStart = False

        if self.programLine == self.programLength:
            self.atEnd = True
        else:
            self.atEnd = False

    def gotoStart(self):
        self.programLine = 0
        self._updateFlags()
        

## REMEMBER THIS ONLY RUNS IF THIS FILE IS NOT AN IMPORT
if __name__ == "__main__":
    print("Hello World")

    tester = program("ARMAddSubRAW.txt")
    for i in range(5):
        print(tester.getNextInstruction())

    # while tester.programLine != tester.programLength:
    #     print(tester.getNextInstruction())

    if tester.atStart:
        print("If the for loop is uncommented, you shouldnt see this")
        while not tester.atEnd:
            print(tester.getNextInstruction())

    else:
        tester.gotoStart()
        print(tester.getNextInstruction())
