from cocotb.types import Logic, LogicArray, Range

def model(Op: LogicArray, Funct: LogicArray, Rd: LogicArray):
    """ model for decoder """
    controls = LogicArray(0, Range(9, 'downto', 0))
    branch = True
    ALUOp = True
    FlagW = LogicArray(0, Range(1, 'downto', 0))

    #need to change the range on the values of Funct to acces the highest bit and the lowest bit
    Funct.range = Range(5, "downto", 0)


    #Main decoder, set controls to be assigned to their appropiate values
    if (Op.integer == 0):
        if (int(Funct[5]) == 1): # could possibly change to -1 on Funct[-1]
            controls = LogicArray('0000101001')
        else:
            controls = LogicArray('0000001001')
    elif (Op.integer == 1):
        if (int(Funct[0]) == 1):
            controls = LogicArray('0001111000')
        else:
            controls = LogicArray('1001110100')
    elif (Op.integer == 2):
        controls = LogicArray('0110100010')
    else:
        controls = LogicArray("0000000000")


    #Output assignment
    RegSrc = controls[9:8]
    ImmSrc = controls[7:6]
    ALUSrc = controls[5]
    MemtoReg = controls[4]
    RegW = controls[3]
    MemW = controls[2]
    Branch = controls[1]
    ALUOp = controls[0]

    # ALUControl setter, basically, add, sub, and, or
    if (ALUOp):
        if(Funct[4:1].integer == 4):
           ALUControl = LogicArray('00')
        elif(Funct[4:1].integer == 2):
           ALUControl = LogicArray('01')
        elif(Funct[4:1].integer == 0):
           ALUControl = LogicArray('10')
        elif(Funct[4:1].integer == 12):
           ALUControl = LogicArray('11')
        else:
            ALUControl = LogicArray('10')

        FlagW[1] = Funct[0]
        FlagW[0] = ((int(Funct[0])==1) and ((ALUControl.integer == 0) or (ALUControl.integer == 1)))
    else:
        ALUControl = LogicArray('00')
        FlagW = LogicArray('00')
    # branch check is here.
    PCS = ((Rd == LogicArray('1111') and RegW) or Branch)
    return { "FlagW":FlagW, "PCS":PCS, "RegW":RegW, "MemW":MemW, "MemtoReg":MemtoReg, "ALUSrc":ALUSrc, "ImmSrc":ImmSrc, "RegSrc":RegSrc, "ALUControl":ALUControl}


