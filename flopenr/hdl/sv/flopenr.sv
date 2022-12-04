module flopenr #(parameter WIDTH=2) (
  input logic               clk, reset, en,
  input logic   [WIDTH-1:0] d,
  output logic  [WIDTH-1:0] q
);

  always_ff @(posedge clk, posedge reset)
    if (reset)          q <= 0;
    else  if (en)       q <= d;

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        clk,
        reset,
        en,
        d,
        q
      );
      #5;
   end
  `endif

endmodule
