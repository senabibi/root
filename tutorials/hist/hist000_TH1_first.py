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

import ROOT # ROOT data analysis framework
import mplhep as hp #Matplotlib extension for HEP style plots
import matplotlib.pyplot as plt #Matplotlib for plotting

#1.Create and fill the histogram
hist=ROOT.TH1F("hist","My first histogram",10,0,10)
my_list=[1,2,3,4,5,6,6,7,8,9,10] #Sample data
for val in my_list:
    hist.Fill(val) #Fill the hist 
#2.Occur ROOT File
with ROOT.TFile.Open("outfile.root", "RECREATE") as outFile:
    outFile.WriteObject(hist, hist.GetName()) #Save the hist to ROOT file
    
#Visulation with matplotlib and mplhep
plt.style.use(hp.style.ROOT)
hp.histplot(hist,histtype="fill", label="My first histogram", color="royalblue")
plt.xlabel("Value") #X-axis label
plt.ylabel("Entries") #Y-axis label
plt.legend()
plt.show()
plt.savefig("histogram.png") #Save the plot as PNG file
print("Histogram saved to histogram.png")