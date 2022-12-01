from model import controller as model

import time
import sys

import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock
from cocotb.types import Logic, LogicArray, Range


@cocotb.test()
async def testController(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    control = model()

    await FallingEdge(dut.clk)

    dut.reset.value = 1
    control.set(1, LogicArray(0, Range(3, 'downto', 0)), LogicArray(0, Range(31, 'downto', 12)))

    await FallingEdge(dut.clk)

    dut.reset.value = 0


    #31-12 = 19to0, 2**20, using 1000 so that the test actually completes
    #before the heat death of the universe
    for Instr_ in range(2**20, 1000):
        Instr = LogicArray(Instr_, Range(31, 'downto', 12))
        if Instr[31:28] == LogicArray('1111') or Instr[27:26] == LogicArray('11'):
            contine
        for ALUFlags in range(16):
            dut.Instr.value = Instr
            dut.ALUFlags.value = LogicArray(ALUFlags, Range(3, 'downto', 0))
            modelResult = control.set(0, LogicArray(ALUFlags, Range(3, 'downto', 0)), Instr)

            await FallingEdge(dut.clk)


            assert dut.MemtoReg.value == int(modelResult["decoder"]["MemtoReg"]), f"HDL and model disagree: {dut.MemtoReg} vs {modelResult}"
            assert dut.ALUSrc.value == int(modelResult["decoder"]["ALUSrc"]), f"HDL and model disagree: {dut.ALUSrc} vs {int(modelResult['decoder']['ALUSrc'])}"
            assert dut.ImmSrc.value == int(modelResult["decoder"]["ImmSrc"].integer), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.RegSrc.value == int(modelResult["decoder"]["RegSrc"].integer), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.ALUControl.value == int(modelResult["decoder"]["ALUControl"].integer), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.PCSrc.value == int(modelResult["condlogic"]["PCSrc"]), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.RegWrite.value == int(modelResult["condlogic"]["RegWrite"]), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
            assert dut.MemWrite.value == int(modelResult["condlogic"]["MemWrite"]), f"HDL and model disagree: {dut.ALUSrc} vs {modelResult['decoder']['ALUSrc']}"
