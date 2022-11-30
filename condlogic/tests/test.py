from model import condlogic as model

import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.types import LogicArray, Logic, Range
from cocotb.clock import Clock

@cocotb.test()
async def testCondlogic(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())


    Cond_ = [LogicArray(x, Range(4-1, 'downto', 0)) for x in range(0, 2**4)]
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

    for Cond in Cond_:
        for ALUFlags in ALUFlags_:
            for FlagW in FlagW_:
                for PCS in PCS_:
                    for RegW in RegW_:
                        for MemW in MemW_:
#                            for reset in reset_:
#                            dut.reset.value = reset
                            print('t')
                            dut.MemW.value = MemW
                            dut.RegW.value = RegW
                            dut.PCS.value = PCS
                            dut.FlagW.value = FlagW
                            dut.ALUFlags.value = ALUFlags
                            dut.Cond.value = Cond

                            CondlogicModel.flopenr(0, ALUFlags, FlagW)
                            modelResult = CondlogicModel.set(Cond, ALUFlags, FlagW, PCS, RegW, MemW)

                            await FallingEdge(dut.clk)
                            print(f"MemW: {MemW}\nRegW: {RegW}\nPCS: {PCS}\nFlagW: {FlagW}\nALUFlags: {ALUFlags}\nCond: {Cond}\n")
                            print(f"SV: PCS: {dut.PCS.value} CondEx : {dut.CondEx.value} Flags : {dut.Flags.value}")
                            assert dut.PCSrc.value == modelResult["PCSrc"], f"HDL and model result disagree: {dut.PCSrc.value} vs {modelResult['PCSrc']}"
