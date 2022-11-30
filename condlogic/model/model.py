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
            return

    def set(self, Cond: LogicArray, ALUFlags: LogicArray, FlagW: LogicArray, PCS: Logic, RegW: Logic, MemW: Logic):
        try:
            self.CondEx = int(condcheck(Cond, self.Flags))
        except:
            self.CondEx = int(condcheck(Cond, self.Flags).integer)
#        self.FlagWrite[1] = (FlagW[1]) & CondEx
#        self.FlagWrite[0] = (FlagW[0]) & CondEx
        RegWrite = int(RegW and self.CondEx)
        MemWrite = int(MemW and self.CondEx)
        PCSrc = int(PCS and self.CondEx)
        return {"RegWrite": RegWrite,
            "MemWrite": MemWrite,
            "PCSrc": PCSrc}
