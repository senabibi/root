## \file
## \ingroup tutorial_hist
## Modern Python version of Hello World example for histograms
##
## Demonstrates ROOT histogram creation with matplotlib/mplhep visualization
##
## \macro_code
##
## \date JULY 2025
## \author Giacomo Parolini (CERN)
## \author Modernized by Nursena Bitirgen (SUMM)

import ROOT
import numpy as np

# Open the file to write the histogram to
with ROOT.TFile.Open("outfile.root", "RECREATE") as outFile:
    values = np.array([1, 2, 3, 3, 3, 4, 3, 2, 1, 0]) 
    # Compute histogram binning (30 bins, range 0-10)
    counts, edges = np.histogram(values, bins=30, range=(0.0, 10.0))  
    h = ROOT.TH1D("histogram", "NumPy-Powered Histogram",len(edges)-1, edges[0], edges[-1])# Bins (n_bins, x_low, x_high)
    # Fill the histogram with the computed counts
    h[...] = counts  
    # Write the histogram to the file
    outFile.WriteObject(h, h.GetName())
   
    
    
 