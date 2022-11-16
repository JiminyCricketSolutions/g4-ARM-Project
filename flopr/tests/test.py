from model import model
import cocotb
from cocotb.triggers import FallingEdge
from cocotb.clock import Clock

@cocotb.test()
async def flopr(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    count = 0
    await FallingEdge(dut.clk)
    for val in range(2**4):
        for reset in range(2):
            dut.d.value = val
            dut.reset.value = reset
            await FallingEdge(dut.clk)
            assert dut.q.value == (val if not reset else 0), f"output q was incorrect on {count} cycle"
            count += 1
