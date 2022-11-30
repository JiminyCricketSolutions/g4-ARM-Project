from cocotb.types import Logic, LogicArray, Range
from condcheck import model as condcheck
import cocotb

class condlogic:
    """ model for condlogic """
    def __init__(self):
        self.Flags = LogicArray('0000')
        self.CondEx = 0

    def flopenr(self, reset: Logic, ALUFlags: LogicArray, FlagW: LogicArray):
        if (bool(reset)):
            self.Flags = LogicArray('0000')
            return
        else:
            if (FlagW[1] == 1 and self.CondEx == 1):
                self.Flags[3:2] = LogicArray(ALUFlags[3:2])

            if (FlagW[1] == 1 and self.CondEx == 1):
                self.Flags[1:0] = LogicArray(ALUFlags[1:0])

            print(f"Model Flags: {self.Flags}")
            return

    def set(self, Cond: LogicArray, ALUFlags: LogicArray, FlagW: LogicArray, PCS: Logic, RegW: Logic, MemW: Logic):
        print(f"Model Cond Array: {Cond}")
        try:
            print(f"Without Except Model CondEx: {condcheck(Cond, self.Flags)}")
            self.CondEx = condcheck(Cond, self.Flags)
        except:
            print(f"With Except Model CondEx: {condcheck(Cond, self.Flags)}")
            self.CondEx = int(condcheck(Cond, self.Flags).integer)
#        self.FlagWrite[1] = (FlagW[1]) & CondEx
#        self.FlagWrite[0] = (FlagW[0]) & CondEx
        RegWrite = int(RegW and self.CondEx)
        MemWrite = int(MemW and self.CondEx)
        PCSrc = int(PCS and self.CondEx)
        print(f"PCS: {PCS}; condEx: {self.CondEx}; PCSrc of Model: {PCSrc}")
        return {"RegWrite": RegWrite,
            "MemWrite": MemWrite,
            "PCSrc": PCSrc}
