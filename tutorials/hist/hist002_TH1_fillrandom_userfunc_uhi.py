import ROOT
import numpy as np
# A function (any dimension) or a formula may reference an already defined formula
form1 = ROOT.TFormula("form1", "abs(sin(x)/x)")
rangeMin = 0.0
rangeMax = 10.0
sqroot = ROOT.TF1("sqroot", "x*gaus(0) + [3]*form1", 0.0, 10.0)
gausScale = 10.0  # [0]
gausMean = 4.0    # [1]
gausVar = 1.0     # [2]
form1Scale = 20.0 # [3]
sqroot.SetParameters(gausScale, gausMean, gausVar, form1Scale)
h1d = ROOT.TH1D("h1d", "Test random numbers", 200, 0.0, 10.0)
# Use our user-defined function to fill the histogram with random values sampled from it.
# Simple approximation using just uniform random numbers
random_numbers = np.array([sqroot.GetRandom() for _ in range(10000)])
counts,_=np.histogram(random_numbers, bins=200, range=(rangeMin, rangeMax))
h1d[...]=counts

# Open a ROOT file and save the formula, function and histogram
with ROOT.TFile.Open("fillrandom_userfunc_py.root", "RECREATE") as myFile:
   myFile.WriteObject(form1, form1.GetName())
   myFile.WriteObject(sqroot, sqroot.GetName())
   myFile.WriteObject(h1d, h1d.GetName())
  