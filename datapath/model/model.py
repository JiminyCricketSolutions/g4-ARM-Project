from cocotb.types import Logic, LogicArray, Range
from condlogic import condlogic
from decoder import model as decoder

class datapath:
      def __init__(self):
          self.cl = condlogic()

      def set(self, reset: Logic, ALUFlags, Instr):
          dec = decoder(Instr[27:26], Instr[25:20], Instr[15:12])
          self.cl.flopenr(reset, ALUFlags, dec["FlagW"])
          cl = self.cl.set(Instr[31:28], ALUFlags, dec["FlagW"], dec["PCS"], dec["RegW"], dec["MemW"])
          return {"decoder":dec,
                "condlogic":cl}

