import model

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge
from cocotb.types import Logic, LogicArray, Range
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def testImem(dut):
    zero = LogicArray(0, Range(31, 'downto', 0))

    ram = model.ram()


    for idx in range(64): 
        addressToRead = LogicArray(idx, Range(31, 'downto', 0))
        dut.a.value = addressToRead
        print("Read addr:", addressToRead)
        await Timer(1, units="ns")
        readValue = LogicArray(dut.rd.value, Range(31, 'downto', 0))
        refReadValue = ram.read(addressToRead)
        print(readValue, refReadValue)
#        assert readValue == refReadValue, 'ERROR: {readValue} vs {refReadValue}'
