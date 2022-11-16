module flopr #(parameter WIDTH=8) (
  input logic               clk, reset,
  input logic   [WIDTH-1:0] d,
  output logic  [WIDTH-1:0] q
);

  always_ff @(posedge clk, posedge reset)
    if (reset)  q <= 0;
    else        q <= d;

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        clk,
        reset,
        d,
        q
      );
      #5;
   end
  `endif

endmodule
