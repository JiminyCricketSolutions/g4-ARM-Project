from cocotb.types import Logic, LogicArray, Range


class arm:
      def __init__(self):
          self.cl = condlogic()

      def set(self, reset: Logic, ALUFlags: LogicArray, Instr: LogicArray):
          dec = decoder(Instr[27:26], Instr[25:20], Instr[15:12])
          self.cl.flopenr(reset, ALUFlags, dec["FlagW"])
          cl = self.cl.set(Instr[31:28], ALUFlags, dec["FlagW"], dec["PCS"], dec["RegW"], dec["MemW"])
          return {"decoder":dec,
                "condlogic":cl}
# attempt at implementing unit testing
# for arm single cycle processor, base level
"""
class arm:
    def __init__(self):
        self.ALUFlags = LogicArray(0, Range(3, 'downto', 0))
        self.RegWrite - Logic('0')
        self.RegSrc = LogicArray(0, Range(1, 'downto', 0))
        self.ImmSrc= LogicArray(0, Range(1, 'downto', 0))
        self.ALUSrc = Logic('0')
        self.ALUControl = LogicArray(0, Range(1, 'downto', 0))
        self.MemWrite = Logic('0')
        self.MemtoReg= Logic('0')
        self.PCSrc = Logic('0')

    def model(reset, PC, Instr, ReadData) -> LogicArray:
        controllerOuput = controller.set(reset, Instr[31:12], self.ALUFlags, self.RegSrc)
        self.RegWrite = controllerOutput["decoder"]["RegWrite"]
        self.ImmSrc = controllerOutput["decoder"]["ImmSrc"]
        self.ALUSrc = controllerOutput["decoder"]["ALUSrc"]
        self.ALUControl = controllerOutput["decoder"]["ALUControl"]
        self.MemWrite = controllerOutput["condlogic"]["MemWrite"]
        self.MemtoReg = controllerOutput["condlogic"]["MemtoReg"]
        self.PCSrc = controllerOutput["condlogic"]["PCSrc"]


        dpOutput = datapath.model(reset, self.RegSrc, self.RegWrite, self.ImmSrc, self.ALUSrc, self.ALUControl, self.MemtoReg, self.PCSrc, Instr, ReadData)

        return (controllerOutput, dpOutput)
"""
