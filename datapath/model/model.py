from mux2 import model as mux
from flopr import model as flopr
from registerfile import registerfile as regfile
from adder import model as adder
from alu import alu as alu
from extender import model as extender

from cocotb.types import Logic, LogicArray, Range

def model(RegSrc: LogicArray, RegWrite: Logic, ImmSrc: LogicArray, ALUSrc: Logic, ALUControl: LogicArray, MemtoReg: Logic, PCSrc: Logic, Instr: LogicArray, ReadData: LogicArray) -> LogicArray:
    ALUFlags = LogicArray(0, Range(3, 'downto', 0))
    PC = LogicArray(0, Range(31, 'downto', 0))
    ALUResult = LogicArray(0, Range(31, 'downto', 0))
    WriteData = LogicArray(0, Range(31, 'downto', 0))
    
    PCNext = PC
    PCPlus4 = PC
    PCPlus8 = PC
    Result = LogicArray(31, 'downto', 0)

    #next PC logic

    PCNext = mux(PCPlus4, Result, PCSrc)
    PC = PCNext
    PCPlus4 = adder(PC, LogicArray('100')) 
    PCPlus8 = adder(PCPlus4, LogicArray('100'))

    #register file logic
    RA1 = mux(Instr[19:16], LogicArray('1111'), RegSrc[0])
    RA2 = mux(Instr[3:0], Instr[15:12], RegSrc[1])
    WriteData = regfile.write(RegWrite, RA1)


    Result = mux(ALUResult, ReadData, MemtoReg)
    ExtImm = extender(Instr[23:0], ImmSrc)
    

    #alu logic
    SrcB = mux(WriteData, ExtImm, AluSrc)
    ALUFlags = alu(SrcA, SrcB, ALUControl, ALUResult)
