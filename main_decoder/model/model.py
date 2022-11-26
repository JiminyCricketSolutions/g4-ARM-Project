from cocotb.types import Logic, LogicArray, Range

def model(Op: LogicArray, Funct: LogicArray, Rd: LogicArray):
    """ model for decoder """
    controls = LogicArray(0, Range(9, 'downto', 0))
    branch = True
    ALUOp = True
    FlagW = LogicArray(0, Range(1, 'downto', 0))

#    print("Op debug", Op)
#    print(Funct, Funct[0])


    #Main decoder
    if (Op.integer == 0):
        if (int(Funct[5]) == 1):
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
    """RegSrc = controls[1:0]
    ImmSrc = controls[3:2]
    ALUSrc = controls[4]
    MemtoReg = controls[5]
    RegW = controls[6]
    MemW = controls[7]
    Branch = controls[8]
    ALUOp = controls[9]
    """
    RegSrc = controls[9:8]
    ImmSrc = controls[7:6]
    ALUSrc = controls[5]
    MemtoReg = controls[4]
    RegW = controls[3]
    MemW = controls[2]
    Branch = controls[1]
    ALUOp = controls[0]
#    print("ALUOp debug:", ALUOp, controls)
#    print("TEST", RegSrc,ImmSrc, ALUSrc, MemtoReg, RegW, MemW, Branch, ALUOp)
    #ALU Decoder
    if (ALUOp):
 #       print("Funct debug x2:", Funct, Funct[4:1])
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

#    print("PCS-->", Rd, RegW, Branch, Rd == LogicArray('1111'))
    PCS = ((Rd == LogicArray('1111') and RegW) or Branch)
    return { "FlagW":FlagW, "PCS":PCS, "RegW":RegW, "MemW":MemW, "MemtoReg":MemtoReg, "ALUSrc":ALUSrc, "ImmSrc":ImmSrc, "RegSrc":RegSrc, "ALUControl":ALUControl}


