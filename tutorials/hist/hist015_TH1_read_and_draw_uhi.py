import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
from mpl_toolkits.mplot3d import Axes3D
from ROOT import TFile
plt.style.use(hep.style.ROOT)
f = TFile("py-hsimple.root")
hpx = f.Get("hpx")
entries = int(hpx.GetEntries())
mean = hpx.GetMean()
std_dev = hpx.GetStdDev()
info_text = f"Entries = {entries}\nMean = {mean:.5f}\nStd Dev = {std_dev:.3f}"
mpl_fig = plt.figure(figsize=(14, 12))
gs = mpl_fig.add_gridspec(3, 2, height_ratios=[1.5, 1.5, 1.5]) 
# --- Plot 1: Basic Histogram ---
ax1 = mpl_fig.add_subplot(gs[0:2, 0])
ax1.set_facecolor("#FFFDD0C8")
hep.histplot(hpx, ax=ax1, histtype='fill', color='#EEAC91', alpha=0.5,edgecolor='blue', linewidth=1.5)
ax1.text(0.65, 0.95, info_text, transform=ax1.transAxes, verticalalignment='top',fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))
# --- Plot 2: Expanded 3D Plot ---
ax2 = mpl_fig.add_subplot(gs[0:2, 1], projection='3d') 
ax2.set_facecolor("#FFFDD0C8")
x = np.array([hpx.GetBinCenter(i) for i in range(1, hpx.GetNbinsX() + 1)])
y = np.zeros_like(x)
z = np.zeros_like(x)
dz = hpx.values()
dx = np.full_like(x, hpx.GetBinWidth(1) * 0.9)
dy = np.full_like(x, 0.2)
ax2.bar3d(x, y, z, dx, dy, dz, color='#EEAC91', edgecolor='darkblue', alpha=0.85)
ax2.text2D(0.55, 0.85, info_text, transform=ax2.transAxes, fontsize=10,bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))
# --- Plot 3: Errorbar Histogram ---
ax3 = mpl_fig.add_subplot(gs[2,:])
ax3.set_facecolor("#FFFDD0C8")
hep.histplot(hpx, ax=ax3, histtype='errorbar', color='darkblue')
ax3.grid(True)
ax3.text(0.90, 0.95, info_text, transform=ax3.transAxes, verticalalignment='top',fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))
mpl_fig.suptitle("Drawing options for one dimensional histograms", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
