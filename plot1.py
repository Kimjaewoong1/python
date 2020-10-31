#%%
import warnings
warnings.simplefilter('ignore')

import time
import random

import numpy as np
import pandas as pd

import requests


import matplotlib as mpl
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import scipy as sp
import statsmodels.api as sm
import sklearn as sk

#맷플롯립 설정
mpl.use('Agg')

#사본 설정
sns.set()
sns.set_style('whitegrid')
sns.set_color_codes()

#시작하기전에 무조건 먼저 실행

plt.rcParams["font.family"] = "Malgun Gothic"

plt.rcParams["font.size"] = 12

plt.rcParams["figure.figsize"] = (14,4)

#글자 깨짐 현상 막기

from scipy import misc # 패키지 임포트
from sklearn.datasets import load_digits

img_rgb = misc.face() #컬러 이미지 로드
img_rgb.shape #데이터의 모양


plt.subplot(221)
plt.imshow(img_rgb, cmap=plt.cm.gray)
plt.axis('off')
plt.title('RGB 컬러 이미지')

plt.subplot(222)
plt.imshow(img_rgb[:,:, 0], cmap=plt.cm.gray) #red 채널 출력
plt.axis('off')
plt.title('Red 채널')

plt.subplot(223)
plt.imshow(img_rgb[:, :, 1], cmap=plt.cm.gray) #green 채널 출력
plt.axis('off')
plt.title('Green 채널')

plt.subplot(224)
plt.imshow(img_rgb[:, :, 2], cmap=plt.cm.gray) #blue 채널 출력
plt.axis('off')workbench.atcion.tasks.test
plt.title('blue 채널')

plt.show()
# %%

# %%

# %%

# %%
