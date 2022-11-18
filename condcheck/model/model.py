from cocotb.types import Logic, LogicArray, Range

def model(Cond: LogicArray, Flags: LogicArray) -> LogicArray:
    """ model for condcheck """
    neg = Flags[0]
    zero = Flags[1]
    carry = Flags[2]
    overflow = Flags[3]

    # weird workaround of bin.BinaryValue or whatever, covert the logic
    # from bools to logicarray and decode to int
    ge = LogicArray(neg == overflow)
    Cond = Cond.integer


    if (Cond == LogicArray('0000').integer):
        return zero
    elif (Cond == LogicArray('0001').integer):
        return LogicArray(not(zero.integer))
    elif (Cond == LogicArray('0010').integer):
        return carry
    elif (Cond == LogicArray('0011').integer):
        return LogicArray(not(carry.integer))
#        return ~carry
    elif (Cond == LogicArray('0100').integer):
        return neg
    elif (Cond == LogicArray('0101').integer):
        return LogicArray(not(neg.integer))
#        return ~neg
    elif (Cond == LogicArray('0110').integer):
        return overflow
    elif (Cond == LogicArray('0111').integer):
        return LogicArray(not(overflow.integer))
#        return ~overflow
    elif (Cond == LogicArray('1000').integer):
        return LogicArray(carry and not(zero.integer))
#        return carry and ~zero
    elif (Cond == LogicArray('1001').integer):
        return LogicArray(not(carry and not(zero.integer)))
#        return ~(carry and ~zero)
    elif (Cond == LogicArray('1010').integer):
        return ge
    elif (Cond == LogicArray('1011').integer):
        return LogicArray(not(ge.integer))
#        return ~ge
    elif (Cond == LogicArray('1100').integer):
        return LogicArray(not(zero.integer) and ge.integer)
#        return ~zero and ge
    elif (Cond == LogicArray('1101').integer):
        return LogicArray(not(not(zero.integer) and ge.integer))
#        return ~(~zero and ge)
    elif (Cond == LogicArray('1110').integer):
        return LogicArray('1')
    else:
        return LogicArray("X")
