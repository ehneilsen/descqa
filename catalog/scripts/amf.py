#!/usr/bin/env python 
import os,sys
import subprocess
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from GalaxyCatalogInterface import loadCatalog
from descqaGlobalConfig import *
from descqaTestConfig import *

# Planck LCDM
om = 0.3089
ob = 0.0486
h  = 0.6774
s8 = 0.816
ns = 0.9667

gc=loadCatalog(sim_catalog)
cosmology=gc.get_cosmology()
print cosmology.H0,cosmology.Om0,cosmology.Ode0

h = cosmology.H0
om = cosmology.Om0
ob = cosmology.Ode0


#EXEPATH=os.path.join(os.path.dirname(os.path.realpath(__file__)),'amf')
EXEPATH='/project/projectdirs/lsst/descqa/src/catalog/scripts/amf'
EXE=os.path.join(EXEPATH,'amf.exe')

# Example call
FNULL = open(os.devnull, 'w')
p = subprocess.call([EXE, "-omega_0", str(om), "-omega_bar", str(ob), "-h", str(h), "-sigma_8", str(s8), "-n_s", str(ns), "-tf", "EH"], stdout=FNULL, stderr=FNULL)

ANALYTIC=os.path.join(EXEPATH,'analytic.dat')
MassFunc = np.loadtxt(ANALYTIC).T

# Plot
fig = plt.figure(figsize=(5, 4))
ax1 = fig.add_axes((0.17, 0.15, 0.79, 0.80))

ax1.loglog(MassFunc[2], MassFunc[3], ls="-", label=r"$z=0$", color="#377EB8", alpha=0.8)

ax1.legend(loc="best")
ax1.set_ylabel(r"dn/dlog(M) [$({\rm Mpc}/h)^3$]")
ax1.set_xlabel(r"Mass [Msun/h]")

plt.grid()
plt.show()
plt.savefig('amf.png')
plt.close()
