import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer
from cocotb.types import LogicArray, Logic
from model import testbench
import ARMMEMLOADER

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def testARMSCtop(dut):
    clock = Clock(dut.clk, 5, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock
    await FallingEdge(dut.clk)
        
    # Reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    
    # Begin testing
    dut.reset.value = 0
    count = 0
    

    # Gather the file that will be used for testing
    filename = ".//ARMSource//ARM453RAW.txt"
    prog = ARMMEMLOADER.program(filename)
    prog.gotoStart()
    print(f"Reading Instruction from {filename}.")
    while not prog.atEnd:
        print(f"#{str(prog.programLine):<3} {prog.program[prog.programLine].strip()}")
        dut.imem.RAM[prog.programLine].setimmediatevalue(LogicArray(prog.program[prog.programLine].strip()).integer)
        prog.getNextInstruction()

    while (count < len(prog.program)*5):
        if (dut.MemWrite.value.binstr == "1"):
            if (dut.DataAdr.value.integer == 100 and dut.WriteData.value.integer == 7):
                break
            elif (dut.DataAdr.value.integer != 97):
                break
        await FallingEdge(dut.clk)
        count += 1
    print(f"mem[{dut.DataAdr.value.integer}]={dut.WriteData.value.integer}")
    print("\n Imem values:")
    for x in range(64-1, 0, -2):
        print(f"{x:<3}{dut.imem.RAM.value[x]} | {x-1:<3}{dut.imem.RAM.value[x-1]}")

    print(dut.arm.dp.rf.rf)

#    for x in range(16):
#        print("R{x:<2} value is: {dut.arm.datapath.regfile[x]}"}
