#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/20
"""

from abc import ABCMeta, abstractmethod
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.model_selection import cross_val_score
from mtlearn import evaluate


class ModelBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, data, params=None):
        self._data = data
        self._pre_data = None
        self._param = params
        self._clf = None
        self._score = None

    @property
    def pre_data(self):
        return self._pre_data

    @pre_data.setter
    def pre_data(self, data):
        self._pre_data = data

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, params):
        self._param = params

    @property
    def clf(self):
        return self._clf

    @clf.setter
    def clf(self, clf):
        self._clf = clf

    @abstractmethod
    def train(self):
        print '{0} model training'.format(self.__class__.__name__)
        pass

    @abstractmethod
    def test(self):
        print '{0} model test'.format(self.__class__.__name__)
        pass

    @abstractmethod
    def predict(self, data):
        print '{0} model predict'.format(self.__class__.__name__)
        self._pre_data = data
        pass

    def cross_validation(self, cv=5):
        self._score = cross_val_score(self._clf, self._data.data, self._data.target, cv=cv)
        pass

    def evaluate(self, test_data):
        print '{0} model evaluate'.format(self.__class__.__name__)
        predict_y = self.predict(test_data)
        evaluate.plot_predict_result(predict_y, test_data)


class RidgeModel(ModelBase):
    def __init__(self, data, params=None):
        super(RidgeModel, self, ).__init__(data, params)
        self._clf = 25

    def train(self):
        super(RidgeModel, self, ).train()
        print 'train'

    def test(self):
        super(RidgeModel, self, ).test()
        print 'test'

    def predict(self, data):
        super(RidgeModel, self, ).predict(data)
        print 'predict'
