import ROOT
import numpy as np
ROOT.gStyle.SetOptStat(0)
c1 = ROOT.TCanvas("c1", "fit residual simple")
h1 = ROOT.TH1D("h1", "h1", 50, -5, 5)
random_numbers = np.random.normal(0.0, 1.0, 2000)
counts, _ = np.histogram(random_numbers, bins=50, range=(-5, 5))
h1[:]=counts
h1.Fit("gaus")
h1.GetXaxis().SetTitle("x")
h1.GetYaxis().SetTitle("y")

rp1 = ROOT.TRatioPlot(h1)
rp1.SetConfidenceIntervalColors("kBlue", "kRed")
rp1.Draw()
c1.Update()
