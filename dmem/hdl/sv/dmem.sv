module dmem (
  input   logic        clk, we,
  input   logic [31:0] a, wd,
  output  logic [31:0] rd
);

  logic [31:0] RAM[63:0];

  assign rd = RAM[a[31:2]]; // word aligned

  always_ff @(posedge clk)
    if (we) RAM[a[31:2]] <= wd;

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        clk,
        we,
        a,
        wd,
        rd
      );
      #5;
   end
  `endif

endmodule
