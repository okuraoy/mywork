#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/20
"""

from sklearn.metrics import explained_variance_score, mean_squared_error
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import numpy as np

rcParams['figure.figsize'] = 15, 6
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
rcParams['axes.unicode_minus'] = False


def plot_predict_result(predict, actual):
    mse = mean_squared_error(actual, predict)
    evs = explained_variance_score(actual, predict)
    # predicts = pd.DataFrame(np.array(predicts), index=test.index)
    plt.plot(actual.inx, actual.data, label="actual", color='blue')
    plt.plot(actual.inx, predict, label="predict", color='red')
    plt.legend(loc='best')
    plt.title('Mean squared error: %.4f,Explained variance score:%.4f' % (mse, evs))
    plt.show()


def plot_importance(importance, index, features):
    pos = np.arange(index.shape[0]) + .5
    # plt.subplot(1, 2, 2)
    plt.barh(pos, importance[index], align='center')
    plt.yticks(pos, features[index])
    plt.xlabel('Importance')
    plt.title('Feature Importance')
    plt.show()
