from cocotb.types import Logic, LogicArray, Range

def model(a: LogicArray, b: LogicArray) -> LogicArray:
    val = (a.integer + b.integer)
    # pretty naive way to test, but since im assuming it will always be 8 bits going for it :)
    # quick fix is add a param val and then change 8 to param
    if (val > 2**8-1):
        val = val-2**8
    return LogicArray(val)
