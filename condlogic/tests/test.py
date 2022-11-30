from model import condlogic as model

import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.types import LogicArray, Logic, Range
from cocotb.clock import Clock

@cocotb.test()
async def testCondlogic(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())


    Cond_ = [LogicArray(x, Range(4-1, 'downto', 0)) for x in range(0, 2**4-1)]
    ALUFlags_ = [LogicArray(x, Range(4-1, 'downto', 0)) for x in range(0, 2**4)]
    FlagW_ = [LogicArray(x, Range(2-1, 'downto', 0)) for x in range(0, 2**2)]
    PCS_ = [0, 1]
    RegW_ = [0, 1]
    MemW_ = [0, 1]
    reset_ = [0, 1]

    CondlogicModel = model()

    await FallingEdge(dut.clk)

    dut.reset.value = 1
    n = LogicArray('0000')
    CondlogicModel.flopenr(1, n, n)


    await FallingEdge(dut.clk)

    dut.reset.value = 0

    for Cond in range(15):
        for ALUFlags in range(16):
            for FlagW in range(4):
                for PCS in range(2):
                    for RegW in range(2):
                        for MemW in range(2):
                            dut.MemW.value = MemW
                            dut.RegW.value = RegW
                            dut.PCS.value = PCS
                            dut.FlagW.value = FlagW
                            dut.ALUFlags.value = ALUFlags
                            dut.Cond.value = Cond
                            print(Cond, ALUFlags, FlagW, PCS, RegW, MemW)
                            CondlogicModel.flopenr(0, LogicArray(ALUFlags, Range(3, 'downto', 0)), LogicArray(FlagW, Range(3, 'downto', 0)))
                            modelResult = CondlogicModel.set(Cond, ALUFlags, FlagW, PCS, RegW, MemW)

                            await FallingEdge(dut.clk)
                            assert dut.RegWrite.value == modelResult["RegWrite"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
                            assert dut.MemWrite.value == modelResult["MemWrite"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
                            assert dut.PCSrc.value == modelResult["PCSrc"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
