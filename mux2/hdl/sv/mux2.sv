module mux2 #(parameter WIDTH=8) (
  input   logic [WIDTH-1:0] d0, d1,
  input logic               s,
  output  logic [WIDTH-1:0] y
);

  assign y = s ? d1 : d0;

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        0,
        d0,
        d1,
        s,
        y
      );
      #5;
   end
  `endif

endmodule
