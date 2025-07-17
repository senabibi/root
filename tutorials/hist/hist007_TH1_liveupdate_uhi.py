import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
from ROOT import TH1F
# Configuration
plt.style.use(hep.style.CMS)
plt.ion()
BINS = 100
RANGE_MIN, RANGE_MAX = -4, 4
K_UPDATE = 500
N_EVENTS = 10000
fig, ax = plt.subplots(figsize=(8, 6), num="The HSUM UHI Example")
total = TH1F('total', 'This is the total distribution', BINS, RANGE_MIN, RANGE_MAX)
total.Sumw2()
# Initialize numpy arrays
bin_edges = np.linspace(RANGE_MIN, RANGE_MAX, BINS + 1)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
counts = {'total': np.zeros(BINS),'main': np.zeros(BINS),'s1': np.zeros(BINS),'s2': np.zeros(BINS)}
# Random number generators
np.random.seed(0)
gauss = lambda loc, scale: np.random.normal(loc, scale)
landau = lambda loc, scale: np.random.standard_cauchy() * scale + loc
def fill_hist(hist_name, x, weight=1.0):
    if RANGE_MIN <= x < RANGE_MAX:
        idx = int((x - RANGE_MIN) / (RANGE_MAX - RANGE_MIN) * BINS)
        counts[hist_name][idx] += weight
# Main loop
for i in range(1, N_EVENTS + 1):
    # Generate values
    xmain = gauss(-1, 1.5)
    xs1 = gauss(-0.5, 0.5)
    xs2 = landau(1, 0.15)
    # Fill histograms
    fill_hist('main', xmain)
    fill_hist('s1', xs1, 0.3)
    fill_hist('s2', xs2, 0.2)
    fill_hist('total', xmain)
    fill_hist('total', xs1, 0.3)
    fill_hist('total', xs2, 0.2)
    # Update plot periodically
    if i % K_UPDATE == 0:
        ax.cla()
        # Calculate statistics
        entries = int(np.sum(counts['total']))
        mean = np.average(bin_centers, weights=counts['total'])
        stddev = np.sqrt(np.average((bin_centers - mean)**2, weights=counts['total']))
        stats_text = f'Entries = {entries}\nMean = {mean:.2f}\nStd Dev = {stddev:.2f}'
        # Plot all four components with original colors
        hep.histplot(counts['main'], bins=bin_edges, histtype='fill', color='gray',alpha=0.5,edgecolor='blue',  linewidth=1.5, ax=ax)
        hep.histplot(counts['s1'], bins=bin_edges,histtype='errorbar', color="blue", alpha=0.7, ax=ax)  
        hep.histplot(counts['s2'], bins=bin_edges,histtype='errorbar', color='blue', alpha=0.7, ax=ax)  
        hep.histplot(counts['total'], bins=bin_edges,histtype='errorbar', color='black', linewidth=2, ax=ax)
        ax.set_title("This is the total distribution", pad=20, fontsize=14, loc='center')
        ax.text(0.95, 0.95, stats_text, transform=ax.transAxes,ha='right', va='top', bbox=dict(facecolor='white', edgecolor='black'))
        # Plot formatting
        ax.set_xlim(RANGE_MIN, RANGE_MAX)
        ax.set_ylim(0, max(counts['total']) * 1.2)
        plt.pause(0.01)
# Keep the final plot open
plt.ioff()
plt.show()