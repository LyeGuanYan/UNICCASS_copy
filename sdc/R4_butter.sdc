###############################################################################
# Created by write_sdc
# Wed Nov  8 16:03:31 2023
###############################################################################
current_design R4_butter
###############################################################################
# Timing Constraints
###############################################################################
create_clock -name clk -period 25.0000 
set_clock_uncertainty 0.2500 clk
set_clock_latency -source -min 4.5000 [get_clocks {clk}]
set_clock_latency -source -max 6.0000 [get_clocks {clk}]
###############################################################################
# Environment
###############################################################################
set_timing_derate -early 0.9500
set_timing_derate -late 1.0500
###############################################################################
# Design Rules
###############################################################################
set_max_transition 0.7500 [current_design]
set_max_fanout 11.0000 [current_design]
