module if_id(
	input  logic          clk, rst_n,
	input  logic [31 : 0] if_instr,
	output logic [31 : 0] id_instr
);

	always_ff @(posedge clk, negedge rst_n) begin
		if(!rst_n) begin
			id_instr <= '0;
		end
		else begin
			id_instr <= if_instr;
		end
	end

endmodule