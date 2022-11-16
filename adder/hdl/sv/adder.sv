module adder #(parameter WIDTH=8) (
  input   logic [WIDTH-1:0] a, b,
  output  logic [WIDTH-1:0] y
);

  assign y = a + b;

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        0,
        a,
        b,
        y
      );
      #5;
   end
  `endif

endmodule
