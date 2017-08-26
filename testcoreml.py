# -*- coding:utf-8 -*-

import coremltools
import logging
import os

if __name__ == '__main__':
    loggingFormat = '%(asctime)s %(lineno)04d %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=loggingFormat, datefmt='%H:%M',)
    
    
    modelFilePath = '%s/%s' % (os.getcwd(), 'MarsHabitatPricePredictor/Resources/MarsHabitatPricer.mlmodel')
    logging.debug(modelFilePath)
    model = coremltools.models.MLModel(modelFilePath)  # 加载mlmodel文件

    # 打印各字段，这些是文件的概要信息
    logging.info('author:              %s' % (model.author))
    logging.info('license:             %s' % (model.license))
    logging.info('short description:   %s' % (model.short_description))
    logging.info('input description:   %s' % (model.input_description))
    logging.info('output description:  %s' % (model.output_description))
 
 	# 打印spec，这里有详细的各字段信息
    logging.info(model.get_spec())

    # 根据输入的三个字段，验证输出值
    dataList = [{'solarPanels':1.0, 'greenhouses':1.0, 'size':1024},
                {'solarPanels':4.0, 'greenhouses':5.0, 'size':10004}]
    for dataItem in dataList:
    	predictions = model.predict(dataItem)
        logging.info('predictions:         %d' % predictions['price'])

