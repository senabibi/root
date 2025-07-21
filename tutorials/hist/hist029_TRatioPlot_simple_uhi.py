import ROOT
import numpy as np
ROOT.gStyle.SetOptStat(0)

c1 = ROOT.TCanvas("c1", "A ratio example")
h1 = ROOT.TH1D("h1", "h1", 50, 0, 10)
h2 = ROOT.TH1D("h2", "h2", 50, 0, 10)
f1 = ROOT.TF1("f1", "exp(- x/[0] )")
f1.SetParameter(0,3)

random_numbers1 = np.array([f1.GetRandom() for _ in range(1900)])
random_numbers2 = np.array([f1.GetRandom() for _ in range(2000)])

counts1, _ = np.histogram(random_numbers1, bins=50, range=(0.0, 10.0))
counts2, _ = np.histogram(random_numbers2, bins=50, range=(0.0, 10.0))

h1[...]=counts1
h2[...]=counts2

import mplhep as hep
import matplotlib.pyplot as plt

hep.histplot(h1)
plt.show()

# h1.Sumw2()
# h2.Scale(1.9/2.)

# print(h1.counts())
# print(h2.counts())

# h1.GetXaxis().SetTitle("x")
# h1.GetYaxis().SetTitle("y")

# rp = ROOT.TRatioPlot(h1,h2)

# c1.SetTicks(0,1)
# rp.GetLowYaxis().SetNdivisions(505)
# c1.Update()
# c1.Draw()
# rp.Draw()

input("Press Enter to continue...")