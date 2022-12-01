from cocotb.types import Logic, LogicArray, Range
from condcheck import model as condcheck
import cocotb

class condlogic:
    """ model for condlogic """
    def __init__(self):
        self.Flags = LogicArray('0000')
        self.CondEx = 0

    def flopenr(self, reset, ALUFlags, FlagW):
        if (bool(reset)):
            self.Flags = LogicArray('0000')
            return
        else:
            if (FlagW[1] and self.CondEx):
                self.Flags[3:2] = (ALUFlags[3:2])

            if (FlagW[0] and self.CondEx):
                self.Flags[1:0] = (ALUFlags[1:0])
            return

    def set(self, Cond: LogicArray, ALUFlags: LogicArray, FlagW: LogicArray, PCS: Logic, RegW: Logic, MemW: Logic):
        try:
            self.CondEx = condcheck(Cond, self.Flags)
        except:
            self.CondEx = int(condcheck(Cond, self.Flags).integer)
        RegWrite = int(RegW and self.CondEx)
        MemWrite = int(MemW and self.CondEx)
        PCSrc = int(PCS and self.CondEx)
        return {"RegWrite": RegWrite,
            "MemWrite": MemWrite,
            "PCSrc": PCSrc}
