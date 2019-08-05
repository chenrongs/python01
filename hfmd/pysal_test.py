# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 14:35
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : pysal_test.py
# @Software: PyCharm
from libpysal.weights.contiguity import Queen
import libpysal
from libpysal import examples
import matplotlib.pyplot as plt
import geopandas as gpd
import random
from pysal.viz.splot.libpysal import plot_spatial_weights


gdf = gpd.read_file(r'C:\Users\RSGG\Desktop\123\city\Anhui.shp')
gdf.head()
weights = Queen.from_dataframe(gdf)
plot_spatial_weights(weights, gdf)
#plt.show()
x = [random.randint(0,100) for i in range(17)]
gdf['test'] = x
fig, ax = plt.subplots(figsize=(12,10), subplot_kw={'aspect':'equal'})
gdf.plot(column='test', scheme='Quantiles', k=5, cmap='GnBu', legend=True, ax=ax)