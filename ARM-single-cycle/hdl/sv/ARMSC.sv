module ARMSC (
  input   logic clk, reset,
  output  logic [31:0]  PC,
  input   logic [31:0]  Instr,
  output  logic         MemWrite,
  output  logic [31:0]  ALUResult, WriteData,
  input   logic [31:0]  ReadData
);

logic [3:0] ALUFlags;
logic       RegWrite,
            ALUSrc, MemtoReg, PCSrc;
logic [1:0] RegSrc, ImmSrc, ALUControl;

controller c(clk, reset, Instr[31:12], ALUFlags,
              RegSrc, RegWrite, ImmSrc,
              ALUSrc, ALUControl,
              MemWrite, MemtoReg, PCSrc);

datapath dp(clk, reset,
            RegSrc, RegWrite, ImmSrc,
            ALUSrc, ALUControl,
            MemtoReg, PCSrc,
            ALUFlags, PC, Instr,
            ALUResult, WriteData, ReadData);






  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        clk,
        reset,
        PC,
        Instr,
        MemWrite,
        ALUResult,
        WriteData,
        ReadData
      );
      #5;
   end
  `endif

endmodule
