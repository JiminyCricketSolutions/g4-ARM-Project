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

    if (Cond == LogicArray('0000').integer):
        return int(zero) #
    elif (Cond == LogicArray('0001').integer):
        return int(not(zero)) #
    elif (Cond == LogicArray('0010').integer):
        return carry #
    elif (Cond == LogicArray('0011').integer):
        return int(not(carry)) #
    elif (Cond == LogicArray('0100').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return neg
    elif (Cond == LogicArray('0101').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(not(neg))
    elif (Cond == LogicArray('0110').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return overflow
    elif (Cond == LogicArray('0111').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(not(overflow))
    elif (Cond == LogicArray('1000').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(carry and not(zero))
    elif (Cond == LogicArray('1001').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(not(carry and not(zero)))
    elif (Cond == LogicArray('1010').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return ge
    elif (Cond == LogicArray('1011').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(not(ge))
    elif (Cond == LogicArray('1100').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(not(zero) and ge)
    elif (Cond == LogicArray('1101').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return int(not(not(zero) and ge))
    elif (Cond == LogicArray('1110').integer):
        # print(f"Cond = {Cond}; Value returned: zero - {int(zero)}")
        return 1
    else:
        return 0
