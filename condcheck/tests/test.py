from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray, Logic, Range
@cocotb.test()
async def testCondcheck(dut):
    for aVal in range(0, 2**4-1):
        for bVal in range(0, 2**4-1):
            dut.Cond.value = aVal
            dut.Flags.value = bVal
            fl = LogicArray(bVal, Range(3, "downto", 0))
            await Timer(1, units="ns")

            modelResult = model(aVal, fl)
            assert (dut.CondEx.value) == int(modelResult), \
                f"HDL and model disagree: {dut.CondEx.value} vs {modelResult}"

