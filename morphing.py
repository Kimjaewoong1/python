import warnings
warnings.simplefilter('ignore')

import importlib
importlib.import_module('mpl_toolkits.mplot3d').__path__
import matplotlib as matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.mpot3d import Axes3D
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import sklean as sk
mpl.use('Agg')
sns.set()
sns.set_style('whitegrid')
sns.set_color_codes()

from sklearn.datasets import fetch_obilvetti_faces

faces = fetch_oblivetti_faces()

f, ax= plt.subplots(1,3)

ax[0].imshow(faces.images[6], cmap = plt.cm.bone) 