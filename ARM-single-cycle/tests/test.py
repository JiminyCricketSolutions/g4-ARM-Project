from model import model
import ARMMEMLOADER

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def testARMSC(dut):


    loadedProgram = ARMMEMLOADER.program("ARMSource/ARMAddSubRAW.txt") # I Came in so that 
    # loadedProgram.getNextInstruction() <- This is a string, pop it in a logicarray
    # Opening the thing
    # for aVal in range(2**4):
    #     for bVal in range(2**4):
    #         dut.a.value = aVal
    #         dut.b.value = bVal
    #         await Timer(1, units="ns")
    #         hdlResult = int(dut.y.value)
    #         modelResult = model(a=dut.a.value, b=dut.b.value).integer
            assert False, "Testing Very Incomplete" #\
                #f"HDL and model disagree: {hdlResult} vs {modelResult}"

