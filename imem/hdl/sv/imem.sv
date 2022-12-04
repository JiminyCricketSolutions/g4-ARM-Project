module imem (
  input   logic [31:0] a,
  output  logic [31:0] rd
);

  logic [31:0] RAM[63:0];

  initial
    $readmemh("memfile.dat", RAM);
    
  assign rd = RAM[a[31:2]]; // word alligned

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        0,
        a,
        rd
      );
      #5;
   end
  `endif

endmodule
