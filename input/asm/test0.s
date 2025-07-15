.text
	csrrw x4, sscratch, x15
	lui sp, 16
	addi t2, zero, 200
	csrrw t2, stimecmp, t2
	addi t4, zero, 34
	csrrw zero, sip, t4
	csrrw zero, sie, t4
	csrrw sp, sscratch, sp
	la t1, trap_handler
	csrrw t1, stvec, t1
	addi t1, zero, 34
	csrrw t1, sstatus, t1
	lui t3, 524290
	csrrw t3, satp, t3
	la t0, _start 
	csrrw t0, sepc, t0
	sret
trap_handler:
	csrrw sp, sscratch, sp
save_reg:
	sw zero, 0(sp)
	sw ra, 4(sp)
	sw gp, 8(sp)
	sw t0, 12(sp)
	sw s0, 28(sp)
	sw s1, 32(sp)
	sw s2, 68(sp)
	sw s3, 72(sp)
	sw s4, 76(sp)
	sw s5, 80(sp)
	sw s6, 84(sp)
	sw s7, 88(sp)
	sw s8, 92(sp)
	sw s9, 96(sp)
	sw s10, 100(sp)
	sw s11, 104(sp)
	csrrw gp, scause, zero
	lui ra, 524288
	addi ra, ra, 1
	beq ra, gp, handle_software_interrupt
	lui ra, 524288
	addi ra, ra, 5
	beq ra, gp, handle_timer_interrupt
	addi ra, zero, 0
	beq ra, gp, handle_address_misaligned
	addi ra, zero, 1
	beq ra, gp, handle_access_fault
	addi ra, zero, 2
	beq ra, gp, handle_illegal_inst
	addi ra, zero, 3
	beq ra, gp, handle_brk_point
	addi ra, zero, 4
	beq ra, gp, handle_load_mis
	addi ra, zero, 5
	beq ra, gp, handle_load_fault
	addi ra, zero, 6
	beq ra, gp, handle_store_mis
	addi ra, zero, 7
	beq ra, gp, handle_store_fault
	addi ra, zero, 8
	beq ra, gp, handle_ecall
	addi ra, zero, 12
	beq ra, gp, handle_inst_page_fault
	addi ra, zero, 13
	beq ra, gp, handle_load_page_fault
	addi ra, zero, 15
	beq ra, gp, handle_store_page_fault
restore_reg:
	lw zero, 0(sp)
	lw ra, 4(sp)
	lw gp, 8(sp)
	lw t0, 12(sp)
	lw s0, 28(sp)
	lw s1, 32(sp)
	lw s2, 68(sp)
	lw s3, 72(sp)
	lw s4, 76(sp)
	lw s5, 80(sp)
	lw s6, 84(sp)
	lw s7, 88(sp)
	lw s8, 92(sp)
	lw s9, 96(sp)
	lw s10, 100(sp)
	lw s11, 104(sp)
	csrrw sp, sscratch, sp
	sret
handle_software_interrupt:
	jal t0, restore_reg
handle_timer_interrupt:
	jal t0, restore_reg
handle_address_misaligned:
	jal t0, restore_reg
handle_access_fault:
	jal t0, restore_reg
handle_illegal_inst:
	jal t0, restore_reg
handle_brk_point:
	jal t0, restore_reg
handle_load_mis:
	jal t0, restore_reg
handle_load_fault:
	jal t0, restore_reg
handle_store_mis:
	jal t0, restore_reg
handle_store_fault:
	jal t0, restore_reg
handle_ecall:
	jal t0, restore_reg
handle_inst_page_fault:
	jal t0, restore_reg
handle_load_page_fault:
	jal t0, restore_reg
handle_store_page_fault:
	jal t0, restore_reg
_start:
addi x2, x0, 8
addi x23, x0, 20
addi x27, x0, 4
addi x25, x0, 12
addi x30, x0, 12
addi x0, x0, 501
addi x1, x0, -800
addi x3, x0, -420
addi x4, x0, 1494
addi x5, x0, 540
addi x6, x0, 223
addi x8, x0, -407
addi x9, x0, 1995
addi x10, x0, 1546
addi x11, x0, -615
addi x12, x0, -952
addi x13, x0, 1414
addi x14, x0, 1488
addi x15, x0, 1948
addi x16, x0, 865
addi x18, x0, -1486
addi x19, x0, 1408
addi x20, x0, -442
addi x21, x0, -1378
addi x22, x0, -1275
addi x24, x0, 1436
addi x26, x0, -174
addi x28, x0, 755
addi x29, x0, 1950
addi x31, x0, 1076
set_up:
addi x7, x0, 10
addi x17, x0, 10
Loop0:
blt x7, x17, Pass
addi x7, x0, 1
addi a7, x0, 10
ecall
addi a7, x0, 5
ecall
csrrs x11, scause, x28
csrrsi x5, sstatus, 14

jalr x26, 219(x24)
Loop1:
jalr x2, 16(x23)
jalr x21, -258(x12)
jalr x15, 102(x31)
jalr x23, -277(x22)
addi a7, x0, 1
ecall
csrrs x28, scause, x22
jalr x3, 406(x0)
Loop2:
jal x18, Pass
jalr x11, -250(x2)
jal x28, Loop0
addi a7, x0, 1
ecall
csrrw x6, sip, x26
addi a7, x0, 12
ecall
csrrc x23, sstatus, x25
Pass:
	addi x31, x0, 88
	jal x0, End
Fail:
	addi x30, x0, 88
End:
