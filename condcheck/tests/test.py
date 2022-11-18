from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray, Logic, Range
@cocotb.test()
async def testCondcheck(dut):
    aVals = [LogicArray(x, Range(4-1, 'downto', 0)) for x in range(0, 2**4)]
    bVals = [LogicArray(x, Range(4-1, 'downto', 0)) for x in range(0, 2**4)]

    for aVal in aVals:
        for bVal in bVals:
            dut.Cond.value = aVal
            dut.Flags.value = bVal
            await Timer(1, units="ns")
            try:
                hdlResult = int(dut.CondEx.value)
            except ValueError:
                hdlResult = -1 # understood as undefined
            try:
                modelResult = model(Cond=dut.Cond.value, Flags=dut.Flags.value).integer
            except ValueError:
                modelResult = -1 # understood as: "undefined" 
            assert hdlResult == modelResult, \
                f"HDL and model disagree: {hdlResult} vs {modelResult}"

