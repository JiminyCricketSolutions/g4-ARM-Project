module hazardUnit (
  input   logic [3:0]   RA1D, RA2D, RA1E, RA2E, WA3M, WA3W, WA3E,
  input   logic         RegWriteM, RegWriteW, MemtoRegE,
  input   logic         PCSrcD, PCSrcE, PCSrcM, PCSrcW, BranchTakenE,
  output  logic [1:0]   ForwardAE, ForwardBE,  // Forward mux control
  output  logic         StallF, StallD, FlushD, FlushE // Pipeline stalls and flushes
);  // This code is derived from the diagram on page 441 of the book, as well
    // as code it was also borrowed from Charles in a different group,
    // however given that it would have been identical anyways
    // Thus is life


logic Match_1E_M, Match_1E_W, Match_2E_M, Match_2E_W;
logic Match_12D_E, LDRStall;
logic PCWrPendingF;

// Check to see if registers match
always_comb begin
    Match_1E_M = (RA1E == WA3M); // Input register is the same as a register that might get written to
    Match_1E_W = (RA1E == WA3W);
    Match_2E_M = (RA2E == WA3M);
    Match_2E_W = (RA2E == WA3W);
    
    // Checks to see if the matching registers matters (i.e., if the registers are not getting written to, don't worry about hazards)
    if      (Match_1E_M & RegWriteM)  ForwardAE = 10; // SrcAE = ALUOutM
    else if (Match_1E_W & RegWriteW)  ForwardAE = 01; // SrcAE = ResultW
    else                              ForwardAE = 00; // SrcAE from Regfile
    if      (Match_2E_M & RegWriteM)  ForwardBE = 10;
    else if (Match_2E_W & RegWriteW)  ForwardBE = 01;
    else                              ForwardBE = 00;

    // LDR Stalling AND Branch Hazards
    Match_12D_E = (RA1D == WA3E) + (RA2D == WA3E);
    LDRStall = Match_12D_E & MemtoRegE;   
    PCWrPendingF = PCSrcD + PCSrcE + PCSrcM; 
    
    StallD = LDRStall;
    StallF = LDRStall + PCWrPendingF;
    FlushE = LDRStall + BranchTakenE;
    FlushD = PCWrPendingF + PCSrcW + BranchTakenE;

  end
  

  // so cocotb will output the wave file in the tests directory
  `ifdef  COCOTB_SIM 
  initial
   begin
      $dumpfile("wave_sv.vcd");
      $dumpvars(
        RA1D, 
        RA2D, 
        RA1E, 
        RA2E, 
        WA3M, 
        WA3W,
        WA3E,
        RegWriteM, 
        RegWriteW, 
        MemtoRegE,
        PCSrcD, 
        PCSrcE, 
        PCSrcM, 
        PCSrcW, 
        BranchTakenE,
        ForwardAE, 
        ForwardBE,
        StallF, 
        StallD, 
        FlushD, 
        FlushE
      );
      #5;
   end
  `endif

endmodule
