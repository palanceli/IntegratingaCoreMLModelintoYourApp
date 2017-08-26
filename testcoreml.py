# -*- coding:utf-8 -*-

import coremltools
import logging
import os

if __name__ == '__main__':
    loggingFormat = '%(asctime)s %(lineno)04d %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=loggingFormat, datefmt='%H:%M',)
    
    
    modelFilePath = '%s/%s' % (os.getcwd(), 'MarsHabitatPricePredictor/Resources/MarsHabitatPricer.mlmodel')
    logging.debug(modelFilePath)
    model = coremltools.models.MLModel(modelFilePath)

    print('author:              %s' % (model.author))
    print('license:             %s' % (model.license))
    print('short description:   %s' % (model.short_description))
    print('input description:   %s' % (model.input_description))
    print('output description:  %s' % (model.output_description))

    print(model.get_spec())

    data = {'solarPanels':1.0, 'greenhouses':1.0, 'size':1024}
    predictions = model.predict(data)
    print('predictions:         %d' % predictions['price'])

