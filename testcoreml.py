# -*- coding:utf-8 -*-

import coremltools
import logging
import os

if __name__ == '__main__':
    loggingFormat = '%(asctime)s %(lineno)04d %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=loggingFormat, datefmt='%H:%M',)
    
    
    modelFilePath = '%s/%s' % (os.getcwd(), 'MarsHabitatPricePredictor/Resources/MarsHabitatPricer.mlmodel')
    logging.debug(modelFilePath)
    model = coremltools.models.MLModel(modelFilePath)  # 

    logging.info('author:              %s' % (model.author))
    logging.info('license:             %s' % (model.license))
    logging.info('short description:   %s' % (model.short_description))
    logging.info('input description:   %s' % (model.input_description))
    logging.info('output description:  %s' % (model.output_description))
 
    logging.info(model.get_spec())

    data = {'solarPanels':1.0, 'greenhouses':1.0, 'size':1024}
    predictions = model.predict(data)
    logging.info('predictions:         %d' % predictions['price'])

