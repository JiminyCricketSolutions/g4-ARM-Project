from model import datapath as model
import time
import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock
from cocotb.types import Logic, LogicArray, Range

import ARMMEMLOADER

@cocotb.test()
async def testDatapath(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    datapath = model()

    dut.reset.value = 1
    datapath.set(1, LogicArray(0, Range(3, 'downto', 0)), LogicArray(0, Range(31, 'downto', 12)))

    await FallingEdge(dut.clk)

    dut.reset.value = 0


    #31-12 = 19to0, 2**20, using 1000 so that the test actually completes
    #before the heat death of the universe
    for Instr_ in range(2**20, 1000):
        Instr = LogicArray(Instr_, Range(31, 'downto', 12))
        if Instr[31:28] == LogicArray('1111') or Instr[27:26] == LogicArray('11'):
            contine
        for ALUFlags in range(16):
            dut.Instr.value = Instr
            dut.ALUFlags.value = LogicArray(ALUFlags, Range(3, 'downto', 0))
            modelResult = datapath.set(0, LogicArray(ALUFlags, Range(3, 'downto', 0)), Instr)

            await FallingEdge(dut.clk)


            assert dut.MemtoReg.value == int(modelResult["decoder"]["MemtoReg"]), f"HDL and model disagree: {dut.MemtoReg} vs {modelResult}"
            assert dut.ALUSrc.value == int(modelResult["decoder"]["ALUSrc"]), f"HDL and model disagree: {dut.ALUSrc} vs {int(modelResult['decoder']['ALUSrc'])}"
            assert dut.ImmSrc.value == int(modelResult["decoder"]["ImmSrc"].integer), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.RegSrc.value == int(modelResult["decoder"]["RegSrc"].integer), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.ALUControl.value == int(modelResult["decoder"]["ALUControl"].integer), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.PCSrc.value == int(modelResult["condlogic"]["PCSrc"]), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.RegWrite.value == int(modelResult["condlogic"]["RegWrite"]), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.MemWrite.value == int(modelResult["condlogic"]["MemWrite"]), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"

#unit testing implementation for datapath, could
#be slightly incomplete, but for the most part should
#be sufficient if values provided are valid instructions.
"""    print("any testing would be insufficent without actual values, otherwise we get undefined states")
    datapath = model()
#    datapath.model()
    t = ARMMEMLOADER.program("ARM453RAW.txt")
#    print(t.gotoStart())
    #print(t.getNextInstruction())
    v = t.getNextInstruction()
    print(v)
    #moduleResult = datapath.module(0, )

# modelResult = datapath.model(0, LogicArray(RegSrc, Range(1, 'downto', 0)), RegWrite, LogicArray(ImmSrc, Range(1, 'downto', 0)), ALUSrc, LogicArray(ALUControl, Range(1, 'downto', 0)), MemtoReg, PCSrc, Instr, LogicArray(ReadData, Range(31, 'downto', 0)))

    
    datapath = model()

    await FallingEdge(dut.clk)
    dut.reset.value = 1
    modelResult = datapath.model(1, LogicArray(0, Range(1, 'downto', 0)), 0, LogicArray(0, Range(1, 'downto', 0)), 0, LogicArray(0, Range(1, 'downto', 0)), 0, 0, LogicArray(0, Range(31, 'downto', 0)), LogicArray(0, Range(31, 'downto', 0)))

    await FallingEdge(dut.clk)
    dut.reset.value = 0
    


    #31-12 = 19to0, 2**20, using 1000 so that the test actually completes
    #before the heat death of the universe
    for Instr_ in range(100, 2**20):
        Instr = LogicArray(Instr_, Range(31, 'downto', 0))
        if Instr[31:28] == LogicArray('1111') or Instr[27:26] == LogicArray('11'):
            contine
        for ReadData in range(32):
            for PCSrc in range(2):
                for MemtoReg in range(2):
                    for ALUControl in range(4):
                        for ALUSrc in range(2):
                            for ImmSrc in range(2):
                                for RegWrite in range(2):
                                    for RegSrc in range(4):
                                        dut.Instr.value = Instr_
                                        dut.ReadData.value = ReadData
                                        dut.PCSrc.value = PCSrc
                                        dut.MemtoReg.value = MemtoReg
                                        dut.ALUControl.value = ALUControl
                                        dut.ALUSrc.value = ALUSrc
                                        dut.ImmSrc.value = ImmSrc
                                        dut.RegWrite.value = RegWrite
                                        dut.RegSrc.value = RegSrc
#                                        print(RegSrc, RegWrite, ImmSrc, ALUSrc)
                                        modelResult = datapath.model(0, LogicArray(RegSrc, Range(1, 'downto', 0)), RegWrite, LogicArray(ImmSrc, Range(1, 'downto', 0)), ALUSrc, LogicArray(ALUControl, Range(1, 'downto', 0)), MemtoReg, PCSrc, Instr, LogicArray(ReadData, Range(31, 'downto', 0)))

                                        await FallingEdge(dut.clk)
                                        print(dut.ALUFlags.value, modelResult["ALUFlags"])
                                        print(dut.ALUResult.value, modelResult["ALUResult"])
                                        print(dut.WriteData.value, modelResult["WriteData"])
                                        print(dut.PC.value, modelResult["PC"])
                                        time.sleep(.7)
#                                        assert dut.ALUFlags.value == modelResult["ALUFlags"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
 #                                       assert dut.ALUResult.value == modelResult["ALUResult"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
  #                                      assert dut.WriteData.value == modelResult["WriteData"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
   #                                     assert dut.PC.value == modelResult["PC"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"

"""
