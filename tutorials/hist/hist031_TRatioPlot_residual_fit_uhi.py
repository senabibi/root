import ROOT
import numpy as np
ROOT.gStyle.SetOptStat(0)
c1 = ROOT.TCanvas("c1", "fit residual simple")
c1.SetLogy()
h1 = ROOT.TH1D("h1", "h1", 50, -5, 5)
h1[:]=np.histogram(np.random.normal(0.0, 1.0, 2000), bins=50, range=(-5, 5))[0]
h1.Fit("gaus")
h1.SetMinimum(0.001)
h1.GetXaxis().SetTitle("x")
h1.GetYaxis().SetTitle("y")
rp1 = ROOT.TRatioPlot(h1)
rp1.Draw()
rp1.GetLowerRefGraph().SetMinimum(-2)
rp1.GetLowerRefGraph().SetMaximum(2)
c1.Update()
