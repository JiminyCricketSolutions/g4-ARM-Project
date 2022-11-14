module pc_logic (
  input   logic [3:0]   rd,
  input   logic         branch,
  input   logic         regw,
  output  logic         pcs
);

// Checks if we are writing to R15 or branching:
// PCS = ((Rd == 15) && RegW) || Branch  (see pg 400 for this equation)

  always_comb
    begin
    
    end







  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        0,
        rd,
        branch,
        regw,
        pcs
      );
      #5;
   end
  `endif

endmodule
