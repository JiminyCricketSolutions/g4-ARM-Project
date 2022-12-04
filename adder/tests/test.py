from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray, Logic, Range
import random

@cocotb.test()
async def testAdder(dut):
    # alot of values stored in here  2**8 = 256
    aVals = [LogicArray(x, Range(8-1, 'downto', 0)) for x in range(0, 2**8)]
    bVals = [LogicArray(x, Range(8-1, 'downto', 0)) for x in range(0, 2**8)]
#    print(aVals)

    # random test of vals so we dont have to wait for the heat death of the universe 
    # of testing every val
    aVals = random.choices(aVals, k=50)
    bVals = random.choices(bVals, k=50)
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


