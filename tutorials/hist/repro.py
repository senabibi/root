import ROOT
import mplhep as hep
import matplotlib.pyplot as plt
import numpy as np 


BINS = 100
RANGE_MIN, RANGE_MAX = -4, 4
K_UPDATE = 500
N_EVENTS = 10000

total = ROOT.TH1F('total', 'This is the total distribution', BINS, RANGE_MIN, RANGE_MAX)
total[...] = np.random.normal(0, 1, BINS)

print(total.values())
print(total.variances())

hep.histplot(total, histtype='errorbar')
plt.show()