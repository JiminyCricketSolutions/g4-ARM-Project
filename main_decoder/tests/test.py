from model import model

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray, Logic, Range

@cocotb.test()
async def testDecoder(dut):
    OpVals = [LogicArray(x, Range(1, 'downto', 0)) for x in range(0, 2**2)]
    FunctVals = [LogicArray(x, Range(5, 'downto', 0)) for x in range(0, 2**6)]
    RdVals = [LogicArray(x, Range(3, 'downto', 0)) for x in range(0, 2**4)]

    for OpVal in OpVals:
        for FunctVal in FunctVals:
            for RdVal in RdVals:
                dut.Op.value = OpVal
                dut.Funct.value = FunctVal
                dut.Rd.value = RdVal
                await Timer(1, units='ns')
                FlagW = dut.FlagW.value
                PCS = dut.PCS.value
                RegW = dut.RegW.value
                MemW = dut.MemW.value
                MemtoReg = dut.MemtoReg.value
                ALUSrc = dut.ALUSrc.value
                ImmSrc = dut.ImmSrc.value
                RegSrc = dut.RegSrc.value
                ALUControl = dut.ALUControl.value
                #print(FunctVal, "<><><>")

                modelResult = model(OpVal, FunctVal, RdVal)

                assert FlagW == modelResult["FlagW"].integer, f"HDL vs MODEL: {FlagW} vs {modelResult['FlagW'].integer}"
                assert PCS  == int(modelResult["PCS"]), f"HDL vs MODEL: {PCS} vs {int(modelResult['PCS'])}"
                assert RegW == int(modelResult["RegW"]), f"HDL vs MODEL: {ReggW} vs {modelResult['RegW']}"
                assert MemW == int(modelResult["MemW"]), f"HDL vs MODEL: {MemW} vs {modelResult['MemW']}"
                assert MemtoReg == int(modelResult["MemtoReg"]), f"HDL vs MODEL: {MemtoReg} vs {modelResult['MemtoReg']}"
                assert ALUSrc  == int(modelResult["ALUSrc"]), f"HDL vs MODEL: {ALUSrc} vs {modelResult['ALUSrc'].integer}"
                assert ImmSrc  == modelResult["ImmSrc"].integer, f"HDL vs MODEL: {ImmSrc} vs {modelResult['ImmSrc'].integer}"
                assert RegSrc == modelResult["RegSrc"].integer, f"HDL vs MODEL: {RegSrc} vs {modelResult['RegSrc'].integer}"
                assert ALUControl == modelResult["ALUControl"].integer, f"HDL vs MODEL: {ALUControl} vs {modelResult['ALUControl'].integer}"
