from cocotb.types import Logic, LogicArray, Range

def hazardUnit(RA1D:LogicArray, RA2D:LogicArray, RA1E:LogicArray, RA2E:LogicArray,
                WA3M:LogicArray, WA3W:LogicArray, WA3E:LogicArray,
                RegWriteM, RegWriteW, MemtoRegE,PCSrcD, PCSrcE, PCSrcM, PCSrcW, BranchTakenE) -> LogicArray:
    """ model for El Grandiose Hazard Unit,
        This Model is in no way a Flip Flop, therefore,
        A class is not made, but a function is used to model its outputs """
    # For a Minute, I forgot how python worked lmaoo

    
    # Go ahead and make the er uh, Return dictionary for use.
    resultsDict = {}
    
    # # If An Input register is the same as a
    # # Register that may be written to, set our match descriptions
    Match_1E_M = (RA1E == WA3M)
    Match_1E_W = (RA1E == WA3W)
    Match_2E_M = (RA2E == WA3M)
    Match_2E_W = (RA2E == WA3W)

    # // Checks to see if the matching registers matters (i.e., if the registers are not getting written to, don't worry about hazards)
    if (Match_1E_M & RegWriteM):
        resultsDict["ForwardAE"] = LogicArray("10") # SrcAE = ALUOutM
    elif (Match_1E_W & RegWriteW):
        resultsDict["ForwardAE"] = LogicArray("01") # SrcAE = ResultW
    else:
        resultsDict["ForwardAE"] = LogicArray("00") # SrcAE from Regfile

    if (Match_2E_M & RegWriteM):  
        resultsDict["ForwardBE"] = LogicArray("10")
    elif (Match_2E_W & RegWriteW):
        resultsDict["ForwardBE"] = LogicArray("01")
    else: 
        resultsDict["ForwardBE"] =LogicArray("00")

    # LDR Stalling AND Branch Hazards
    Match_12D_E = (RA1D == WA3E) or (RA2D == WA3E)
    LDRStall = Match_12D_E and MemtoRegE
    PCWrPendingF = PCSrcD or PCSrcE or PCSrcM
    
    resultsDict["StallD"] = LDRStall
    resultsDict["StallF"] = LDRStall or PCWrPendingF
    resultsDict["FlushE"] = LDRStall or BranchTakenE
    resultsDict["FlushD"] = PCWrPendingF or PCSrcW or BranchTakenE





    # EXPECTED RETURN VALUES
    # ForwardAE, ForwardBE, StallF, StallD, FlushD, FlushE
    return resultsDict
