from model import model

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def testDatapath(dut):

