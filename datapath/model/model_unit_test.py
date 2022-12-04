from mux2 import model as mux
from registerfile import registerfile as regfile
from adder import model as adder
from alu import alu as alu
from extender import model as extender

from cocotb.types import Logic, LogicArray, Range

class datapath:
    def __init__(self):
        self.PC = LogicArray(0, Range(31, 'downto', 0))
        self.ALUFlags = LogicArray(0, Range(3, 'downto', 0))
        self.Result = LogicArray(0, Range(31, 'downto', 0))
        # set PCPLUS4 to PC+4 at start so it starts at mem addr 4 or whateva
        self.PCPlus4 = LogicArray(0, Range(31, 'downto', 0))
        self.regfile_1 = regfile()
        self.ALUResult = LogicArray(0, Range(31, 'downto', 0))

    def model(self, reset: Logic, RegSrc: LogicArray, RegWrite: Logic, ImmSrc: LogicArray, ALUSrc: Logic, ALUControl: LogicArray, MemtoReg: Logic, PCSrc: Logic, Instr: LogicArray, ReadData: LogicArray):
        #next PC logic
        PCNext = mux(self.PCPlus4, self.Result, PCSrc)

        #fake a flopr
        if (bool(reset)):
            self.PC = LogicArray(0, Range(31, 'downto', 0))
        else:
            self.PC = PCNext


        self.PCPlus4 = adder(self.PC, LogicArray('100'))
        PCPlus8 = adder(self.PCPlus4, LogicArray('100'))

        #register file logic
        RA1 = mux(Instr[19:16], LogicArray('1111'), RegSrc[0])
        RA2 = mux(Instr[3:0], Instr[15:12], RegSrc[1])

        self.regfile_1.write(RegWrite, Instr[15:12], self.Result)
        SrcA = LogicArray(self.regfile_1.read(RA1, PCPlus8).integer, Range(31, 'downto', 0))


        WriteData = self.regfile_1.read(RA2, PCPlus8)

        self.Result = mux(self.ALUResult, ReadData, MemtoReg)

#        print(Instr, "<>", Instr[23:0])
        ExtImm = extender(ImmSrc, Instr[23:0])


        #alu logic
#        print(WriteData, ExtImm, ALUSrc)

        SrcB = mux(WriteData, ExtImm, ALUSrc)

 #       print(WriteData, ExtImm, ALUSrc)
  #      print("||||||", SrcA, SrcB, ALUSrc)

   #     print("ALUControl", ALUControl, SrcB, SrcA)
        self.ALUResult, self.ALUFlags = alu(SrcA, SrcB, ALUControl)
    #    print(self.ALUResult, self.ALUFlags, "\n\n")
        return {"ALUFlags": self.ALUFlags,
                "PC": self.PC,
                "ALUResult": self.ALUResult,
                "WriteData": WriteData}
