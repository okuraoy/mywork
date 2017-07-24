#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/20
"""

from model_base import ModelBase


class RidgeModel(ModelBase):
    def __init__(self, data, params=None):
        super(RidgeModel, self, ).__init__(data, params)

    def train(self):
        super(RidgeModel, self, ).train()
        print 'train'

    def test(self):
        super(RidgeModel, self, ).test()
        print 'test'

    def predict(self, data):
        super(RidgeModel, self, ).predict(data)
        print 'predict'
