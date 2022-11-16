from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray, Logic, Range

@cocotb.test()
async def test4_33(dut):
    # alot of values stored in here  2**8 = 256
    aVals = [LogicArray(x, Range(8-1, 'downto', 0)) for x in range(0, 2**8)]
    bVals = [LogicArray(x, Range(8-1, 'downto', 0)) for x in range(0, 2**8)]
#    print(aVals)

    # even more maths doing 256*256, but hey its exhaustive :)
    for aVal in aVals:
        for bVal in bVals:
            dut.a.value = aVal.integer
            dut.b.value = bVal.integer
            await Timer(1, units="ns")
            hdlResult = int(dut.y.value)
            modelResult = model(a=dut.a.value, b=dut.b.value).integer
            assert hdlResult == modelResult, \
                f"HDL and model disagree: {hdlResult} vs {modelResult}... {aVal} .. {bVal}"


