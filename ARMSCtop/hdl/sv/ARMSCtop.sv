module ARMSCtop (
  input   logic       clk, reset,
  output  logic [31:0] WriteData, DataAdr,
  output  logic       MemWrite
);

  logic [31:0] PC, Instr, ReadData;

  // instantiate processor and memories
  ARMSC arm(clk, reset, PC, Instr, MemWrite, DataAdr, WriteData, ReadData);
  imem  imem(PC, Instr);
  dmem  dmem(clk, MemWrite, DataAdr, WriteData, ReadData);

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        clk,
        reset,
        WriteData,
        DataAdr,
        MemWrite
      );
      #5;
   end
  `endif

endmodule
