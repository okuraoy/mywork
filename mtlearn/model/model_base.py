#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/20
"""

from abc import ABCMeta, abstractmethod
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
from mtlearn import evaluate


class ModelBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, data, params=None, m_file=None):
        self._data = data
        self._param = params
        self._model_file = m_file
        self._pre_result = None
        self._clf = None
        self._score = None

    @property
    def pre_result(self):
        return self._pre_result

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, params):
        self._param = params

    @property
    def clf(self):
        return self._clf

    @abstractmethod
    def train(self):
        print '{0} model training'.format(self.__class__.__name__)
        self._clf.fit(self._data.data, self._data.target)
        joblib.dump(self._clf, self._model_file)
        pass

    @abstractmethod
    def test(self):
        print '{0} model test'.format(self.__class__.__name__)
        self._cross_validation()
        pass

    @abstractmethod
    def predict(self, data):
        print '{0} model predict'.format(self.__class__.__name__)
        save_clf = joblib.load(self._model_file)
        if save_clf:
            self._clf = save_clf
        self._pre_result = self._clf.predict(data)

    def _cross_validation(self, cv=5):
        self._score = cross_val_score(self._clf, self._data.data, self._data.target, cv=cv)

    def evaluate(self, test_data):
        print '{0} model evaluate'.format(self.__class__.__name__)
        self.predict(test_data)
        evaluate.plot_predict_result(self._pre_result, test_data)


class RidgeModel(ModelBase):
    """
      岭回归模型
    """

    def __init__(self, data, params=None):
        super(RidgeModel, self, ).__init__(data, params)
        self._clf = RidgeCV(alphas=[0.1, 0.5, 1.0, 5.0, 10.0])

    def train(self):
        super(RidgeModel, self, ).train()
        print 'ridge cv values:' % self._clf.cv_values_
        print 'ridge coef:' % self._clf.coef_
        print 'Ridge intercept:' % self._clf.intercept_
        print 'Ridge alpha:' % self._clf.alpha_

    def test(self):
        super(RidgeModel, self, ).test()
        self._score = -self._score['neg_mean_squared_error']
        print 'Accuracy mse / mean / std: %0.2f %0.2f (+/- %0.2f)' % (
            self._score, self._score.mean(), self._score.std() * 2)

    def predict(self, data):
        super(RidgeModel, self, ).predict(data)


class GBDTModel(ModelBase):
    """
     GBDT算法模型
    """

    def __init__(self, data, params=None):
        super(GBDTModel, self, ).__init__(data, params)
        self._clf = GradientBoostingRegressor(n_estimators=300, learning_rate=0.01,
                                              max_depth=3, random_state=0, loss='ls')

    def train(self):
        super(GBDTModel, self, ).train()
        # print 'ridge cv values:' % self._clf.cv_values_
        # print 'ridge coef:' % self._clf.coef_
        # print 'Ridge intercept:' % self._clf.intercept_
        # print 'Ridge alpha:' % self._clf.alpha_

    def test(self):
        super(GBDTModel, self, ).test()
        feature_importance = self._clf.feature_importances_
        mse = -self._score['neg_mean_squared_error']
        print 'MSE / Mean / Std: %0.2f %0.2f (+/- %0.2f)' % (mse, mse.mean(), mse.std() * 2)

    def predict(self, data):
        super(GBDTModel, self, ).predict(data)
