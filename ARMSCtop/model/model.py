from cocotb.types import Logic, LogicArray, Range
from top import arm as arm
from imem import ram as imem
from dmem import ram as dmem

# would be utilized for a unit test implementation,
# but due to time constraints, the test.py uses a 
# data flow model inorder to ascertain its' outputs.
# other lower units are tested for accuracy though.
class testbench:
    def __init__(self):
        self.arm = arm()
        self.imem = imem()
        self.dmem = dmem()

    def model(reset, WriteData, DataAdr, MemWrite):
        self.top.model(reset, WriteData, DataAdr, MemWrite)
        self.imem.read(PC, Instr)
        self.dmem.write(MemWrite, DataAdr, WriteData)
