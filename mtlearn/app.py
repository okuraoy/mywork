#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by guanlei on 2017/7/20
"""

import sys
from optparse import OptionParser
import time
import logging
import datasets
from model.model_base import RidgeModel, GBDTModel

GLOBAL_ARGS = {}


def get_model(data):
    if GLOBAL_ARGS['model'] == 'linear':
        print ""
        # estimator = LinearRegression()
    elif GLOBAL_ARGS['model'] == 'ridge':
        estimator = RidgeModel(data)
    elif GLOBAL_ARGS['model'] == 'rf':
        print ""
        # estimator = RandomForestRegressor(n_estimators=200, max_depth=3, max_features='sqrt',
        #                                   random_state=0, n_jobs=2)
    elif GLOBAL_ARGS['model'] == 'gbrt':
        estimator = GBDTModel(data)
        # estimator = GradientBoostingRegressor(n_estimators=300, learning_rate=0.01,
        #                                       max_depth=3, random_state=0, loss='ls')
    return estimator


def process_input():
    if len(sys.argv) > 1:
        msg_usage = "pcs_predict [ -m <mode>][-s <stage>] arg1[,arg2..]"
        opt_parser = OptionParser(msg_usage)
        opt_parser.add_option(
            "-m", "--model", action="store", type="string", dest="model")
        opt_parser.add_option(
            "-a", "--stage", action="store", type="string", dest="stage")
        # opt_parser.add_option(
        #     "-f", "--file", action="store", type="string", dest="file")
        (options, args) = opt_parser.parse_args(sys.argv)
        GLOBAL_ARGS['model'] = options.model
        GLOBAL_ARGS['stage'] = options.stage
        # GLOBAL_ARGS['file'] = options.file
        GLOBAL_ARGS['args'] = args
    else:
        print u"请选择模型,linear:线性回归模型,ridge:岭回归模型,rf:随机森林模型,gbrt:GBRT模型,请输入:"
        model_type = raw_input()
        while not (model_type in ['linear', 'ridge', 'rf', 'gbrt']):
            print u"不好意思，您选择的模型无效,请重新输入:"
            model_type = raw_input()
        GLOBAL_ARGS['model'] = model_type.strip()

        print u"请选择模型操作：train:模型训练, test:模型验证, predict:模型预测"
        stage = raw_input()
        while not (stage in ['train', 'test', 'predict']):
            print u"不好意思，您选择的操作无效,请重新输入:"
            stage = raw_input()
        GLOBAL_ARGS['stage'] = stage.strip()

        # print u"请输入数据文件路径,格式:'D:\\data.txt'"
        # file_path = raw_input()
        # while file_path is None:
        #     print u"不好意思，请输入数据文件路径:"
        #     file_path = raw_input()
        # GLOBAL_ARGS['file'] = file_path.strip()

        print u"请输入模型参数,以','隔开"
        args = raw_input()
        GLOBAL_ARGS['args'] = args.strip()


def main():
    logging.info("load data begin...")
    pcs = datasets.load_pcs_data()
    logging.info("load data begin...")
    estimator = get_model(pcs)
    estimator.test()
    logging.info("model test end...")


if __name__ == '__main__':
    # try:
    process_input()
    main()
    print u'程序执行完成，谢谢！'
    time.sleep(5)
    # except Exception, e:
    #     print str(e)
    #     print u'程序异常，程序将在10s后退出'
    #     time.sleep(5)
