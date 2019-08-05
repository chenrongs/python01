import seaborn as sns
from scipy import stats, integrate
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
from matplotlib.font_manager import FontProperties
myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=myfont.get_name())


np.random.seed(sum(map(ord, "distributions")))#每次产生的随机数相同
x = np.random.gamma(6, size=200)
plt.figure(figsize=(15, 10))
#sns.set_style('whitegrid')
sns.distplot(x, kde=False, fit=stats.gamma)
plt.xlabel('数量/个')
plt.ylabel("成立年限/年")
plt.show()