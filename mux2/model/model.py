from cocotb.types import Logic, LogicArray, Range

def model(d0: LogicArray, d1: LogicArray, s: LogicArray) -> LogicArray:
    return d1 if s else d0
