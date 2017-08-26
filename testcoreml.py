# -*- coding:utf-8 -*-

import coremltools

modelFilePath = '/Users/palance/Downloads/IntegratingaCoreMLModelintoYourApp/MarsHabitatPricePredictor/Resources/MarsHabitatPricer.mlmodel'
model = coremltools.models.MLModel(modelFilePath)

print('author:              %s' % (model.author))
print('license:             %s' % (model.license))
print('short description:   %s' % (model.short_description))
print('input description:   %s' % (model.input_description))
print('output description:  %s' % (model.output_description))

print(model.get_spec())

data = {'solarPanels':1.0, 'greenhouses':1.0, 'size':1024}
predictions = model.predict(data)
print('predictions:         %d' % data.price)