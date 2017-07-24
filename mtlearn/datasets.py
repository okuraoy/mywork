#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.datasets.base import Bunch
from os.path import join

PATH = "d:\\data"

# class Bunch(dict):
#     """Container object for datasets
#     Dictionary-like object that exposes its keys as attributes.
#
#     See: sklearn.datasets.base.py Bunch
#     """
#
#     def __init__(self, **kwargs):
#         super(Bunch, self).__init__(kwargs)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def __dir__(self):
#         return self.keys()
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(key)
#
#     def __setstate__(self, state):
#         # Bunch pickles generated with scikit-learn 0.16.* have an non
#         # empty __dict__. This causes a surprising behaviour when
#         # loading these pickles scikit-learn 0.17: reading bunch.key
#         # uses __dict__ but assigning to bunch.key use __setattr__ and
#         # only changes bunch['key']. More details can be found at:
#         # https://github.com/scikit-learn/scikit-learn/issues/6196.
#         # Overriding __setstate__ to be a noop has the effect of
#         # ignoring the pickled __dict__
#         pass


def parse_date(x):
    return pd.datetime.strptime(x, '%Y-%m-%d')


def load_pcs_data():
    # column: date,pcs,f1,f2,...

    df = pd.read_csv(join(PATH, "am000975-pcs.csv"), parse_dates=['date'], date_parser=parse_date)
    df.sort_values(by='date')
    columns = np.array(df.columns.values)
    feature_name = columns[1:]
    tmp_data = np.array(df)
    inx_data = tmp_data[:, 0]
    target = tmp_data[:, 1]
    data = tmp_data[:, 2:]

    # print target
    print data.shape

    return Bunch(data=data, target=target, feature_name=feature_name, inx=inx_data)


if __name__ == '__main__':
    load_pcs_data()
