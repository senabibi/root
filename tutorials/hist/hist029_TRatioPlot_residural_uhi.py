import ROOT
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
from scipy.stats import norm

h1 = ROOT.TH1D("h1", "h1", 50, -5, 5)
h1.FillRandom("gaus", 2000)
plt.style.use(hep.style.ROOT) 

bin_contents = np.array([h1.GetBinContent(i) for i in range(1, 51)])
bin_edges = np.array([h1.GetBinLowEdge(i) for i in range(1, 52)])
# Fit yap
data = np.repeat((bin_edges[:-1] + bin_edges[1:])/2, bin_contents.astype(int))
mu, sigma = norm.fit(data)
# Plot oluştur
fig, (ax, rax) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
plt.subplots_adjust(hspace=0.07)
# Ana histogram
hep.histplot(bin_contents, bins=bin_edges, ax=ax, label="Data", yerr=True)
# Fit eğrisi
x = np.linspace(-5, 5, 200)
ax.plot(x, norm.pdf(x, mu, sigma)*sum(bin_contents)*(10/50), 'r-')
expected = norm.pdf((bin_edges[:-1] + bin_edges[1:])/2, mu, sigma)*sum(bin_contents)*(10/50)
ratio = bin_contents/expected
hep.histplot(ratio, bins=bin_edges, ax=rax, yerr=np.sqrt(bin_contents)/expected)
rax.axhline(1, color='gray', linestyle='--')
ax.legend()

plt.show()