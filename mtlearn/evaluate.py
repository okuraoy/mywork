#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/20
"""

from sklearn.metrics import mean_squared_error
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 15, 6
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
rcParams['axes.unicode_minus'] = False


def plot_predict_result(predict, actual):
    mse = mean_squared_error(actual, predict)
    # predicts = pd.DataFrame(np.array(predicts), index=test.index)
    plt.plot(actual.inx, actual.data, label="actual", color='blue')
    plt.plot(actual.inx, predict, label="predict", color='red')
    plt.legend(loc='best')
    plt.title('MSE: %.4f' % mse)
    plt.show()
