from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray, Logic, Range
@cocotb.test()
async def test4_33(dut):
    aVals = [LogicArray(x, Range(8-1, 'downto', 0)) for x in range(0, 2**8)]
    bVals = [LogicArray(x, Range(8-1, 'downto', 0)) for x in range(0, 2**8)]
    sel =  [0, 1]
    for aVal in aVals:
        for bVal in bVals:
            for s in sel:
                dut.d0.value = aVal
                dut.d1.value = bVal
                dut.s.value = s
                await Timer(1, units="ns")
                hdlResult = int(dut.y.value)
                modelResult = model(d0=dut.d0.value, d1=dut.d1.value, s=dut.s.value).integer
                assert hdlResult == modelResult, \
                f"HDL and model disagree: {hdlResult} vs {modelResult}"

