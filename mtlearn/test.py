#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/24
"""

from model.ridge_model import RidgeModel

if __name__ == '__main__':
    d = [1, 2, 3, 4, 5]
    p = ['a', 'b', 'c']
    m = RidgeModel(d, params=p)
    m.train()
    m.test()
    m.predict([2, 3, 4])
