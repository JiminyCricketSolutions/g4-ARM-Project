from model import hazardUnit as model

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def testHazardUnit(dut):
    
    RA1D = 0
    RA2D = 0
    RA1E = 0
    RA2E    = 0
    WA3M    = 0
    WA3W    = 0
    WA3E    = 0
    RegWriteM   = 0
    RegWriteW   = 0
    MemtoRegE   = 0
    PCSrcD  = 0
    PCSrcE  = 0
    PCSrcM  = 0
    PCSrcW  = 0
    BranchTakenE    = 0

    # Set Values of Dut
    dut.RA1D.value          = RA1D
    dut.RA2D.value          = RA2D
    dut.RA1E.value          = RA1E
    dut.RA2E.value          = RA2E
    dut.WA3M.value          = WA3M
    dut.WA3W.value          = WA3W
    dut.WA3E.value          = WA3E
    dut.RegWriteM.value     = RegWriteM
    dut.RegWriteW.value     = RegWriteW
    dut.MemtoRegE.value     = MemtoRegE
    dut.PCSrcD.value        = PCSrcD
    dut.PCSrcE.value        = PCSrcE
    dut.PCSrcM.value        = PCSrcM
    dut.PCSrcW.value        = PCSrcW
    dut.BranchTakenE.value  = BranchTakenE

    # Wait and set
    await Timer(1, units="ns")

    #HDL Results dict
    hdlResult = {} # Initial Declare, no call again
    hdlResult["ForwardAE"] = dut.ForwardAE.value
    hdlResult["ForwardBE"] = dut.ForwardBE.value
    hdlResult["StallF"]    = dut.StallF.value
    hdlResult["StallD"]    = dut.StallD.value
    hdlResult["FlushD"]    = dut.FlushD.value
    hdlResult["FlushE"]    = dut.FlushE.value

    modelResult = model(RA1D, RA2D, RA1E, RA2E, WA3M, WA3W, WA3E,
                RegWriteM, RegWriteW, MemtoRegE,PCSrcD, PCSrcE, PCSrcM, PCSrcW, BranchTakenE)

    # Check
    
    assert hdlResult == modelResult, \
    f"HDL and model disagree: {hdlResult} vs {modelResult}"





