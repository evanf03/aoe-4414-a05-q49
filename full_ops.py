# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv

# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors

# Output: Outputs the channel count, width count, height count, and number of mathematical operations performed

# Written by Evan Fillmore

# import Python modules
import sys # argv
import math 

# initialize script arguments
c_in = float("nan")
n_wv = float("nan")

# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
else:
    print(\
        'Usage: '\
        'python3 full_ops.py c_in n_wv'\
    )
    exit()

# write script below this line

h_out = 0
w_out = 0
adds = n_wv*c_in
divs = 0
muls = n_wv*c_in
c_out = c_in

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed