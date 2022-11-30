from cocotb.types import Logic, LogicArray, Range

def model(Cond: LogicArray, Flags: LogicArray):
    """ model for condcheck """
    neg = Flags[3]
    zero = Flags[2]
    carry = Flags[1]
    overflow = Flags[0]
    
    # weird workaround of bin.BinaryValue or whatever, covert the logic
    # from bools to logicarray and decode to int
    ge = int((neg == overflow))
#    Cond = Cond.integer
    print(f"You have Successfully Called CondCheck with \n Cond: {Cond}, and Flags : {Flags}")

    if (Cond.integer == LogicArray('0000').integer):
        return int(zero)
    elif (Cond.integer == LogicArray('0001').integer):
        print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        return int(not(zero))
    elif (Cond.integer == LogicArray('0010').integer):
        return carry
    elif (Cond.integer == LogicArray('0011').integer):
        return int(not(carry))
    elif (Cond.integer == LogicArray('0100').integer):
        return neg
    elif (Cond.integer == LogicArray('0101').integer):
        return int(not(neg))
    elif (Cond.integer == LogicArray('0110').integer):
        return overflow
    elif (Cond.integer == LogicArray('0111').integer):
        return int(not(overflow))
    elif (Cond.integer == LogicArray('1000').integer):
        
        return int(carry and not(zero))
    elif (Cond.integer == LogicArray('1001').integer):
        return int(not(carry and not(zero)))
    elif (Cond.integer == LogicArray('1010').integer):
        return ge
    elif (Cond.integer == LogicArray('1011').integer):
        return int(not(ge))
    elif (Cond.integer == LogicArray('1100').integer):
        return int(not(zero) and ge)
    elif (Cond.integer == LogicArray('1101').integer):
        return int(not(not(zero) and ge))
    elif (Cond.integer == LogicArray('1110').integer):
        return 1
    else:
        return 0
