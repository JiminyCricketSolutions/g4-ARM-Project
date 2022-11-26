from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import Logic, LogicArray, Range

from random import randrange

@cocotb.test()
async def test_extender(dut):

    for numIter in range(10):
        instr = LogicArray(randrange(2**23), Range(23, 'downto', 0))
        print(f'{instr}')
        dut.Instr.value = instr
        
        for immsrc in range(3):
            dut.ImmSrc.value = LogicArray(immsrc, Range(1, 'downto', 0))
            await Timer(1, units="ns")
            assert LogicArray(dut.ExtImm.value, Range(31, 'downto', 0)) == LogicArray(model(dut.ImmSrc.value, dut.Instr.value), Range(31, 'downto', 0)), \
                f"{instr}, {immsrc}: {dut.ExtImm.value} vs {model(dut.ImmSrc.value, dut.Instr.value)}"
