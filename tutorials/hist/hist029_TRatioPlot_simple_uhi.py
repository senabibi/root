import ROOT
import numpy as np
ROOT.gStyle.SetOptStat(0)
c1 = ROOT.TCanvas("c1", "A ratio example")
h1 = ROOT.TH1D("h1", "h1", 50, 0, 10)
h2 = ROOT.TH1D("h2", "h2", 50, 0, 10)
f1 = ROOT.TF1("f1", "exp(- x/[0] )")
f1.SetParameter(0,3)
h1[...]=np.histogram(np.array([f1.GetRandom() for _ in range(1900)]), bins=50, range=(0.0, 10.0))[0]
h2[...]=np.histogram(np.array([f1.GetRandom() for _ in range(2000)]), bins=50, range=(0.0, 10.0))[0]
import mplhep as hep
import matplotlib.pyplot as plt
hep.histplot(h1)
plt.show()