import ROOT
import numpy as np    
# Create a histogram using ROOT
h = ROOT.TH1D("h1d", "Test random numbers", 200, 0.0, 10.0) 
# mean = 0.0, standard deviation = 1.0
random_numbers = np.random.normal(0.0, 1.0, 10000)
# Create a numpy histogram with the same binning
counts,_=np.histogram(random_numbers, bins=200, range=(0.0, 10.0))
h[:]=counts
with ROOT.TFile.Open("fillrandom_py.root", "RECREATE") as myfile:
    myfile.WriteObject(h, h.GetName())
