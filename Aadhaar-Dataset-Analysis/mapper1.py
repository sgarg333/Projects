#Count the no. of identities in each state.

#!/usr/bin/python

import sys

sys.stdin.readline()
for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) != 0:
        R, E_A, State, District, S_D, PinCode, Gender, Age, Aadhaar_generated, E_R, R_p_e, R_p_m_n = data
        print "{0}\t{1}".format(State, Aadhaar_generated)
