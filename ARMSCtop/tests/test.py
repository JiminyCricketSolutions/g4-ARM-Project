from model import model
import ARMMEMLOADER

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def testARMSCtop(dut):

    # This Section of code loads an arm program into the processor.
    prog = ARMMEMLOADER.program("ARMAddSubRAW.txt")
    prog.gotoStart()
    while not prog.atEnd:
        #   _________________ The part below the underscores may need to change to our specific design.
        dut.datapath.imem.mem[prog.programLine].setimmediatevalue(LogicArray(prog.getNextInstruction()).integer)

    # for aVal in range(2**4):
    #     for bVal in range(2**4):
    #         dut.a.value = aVal
    #         dut.b.value = bVal
    #         await Timer(1, units="ns")
    #         hdlResult = int(dut.y.value)
    #         modelResult = model(a=dut.a.value, b=dut.b.value).integer
    #         assert hdlResult == modelResult, \
    #             f"HDL and model disagree: {hdlResult} vs {modelResult}"

