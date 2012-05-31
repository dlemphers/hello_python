import sys
import importlib
import logging

class Pipeline(object):

    STEPS = ['pipes.steps.uppercase']

    def __init__(self):
        self.load_components()

    def create_object(self, module, object_name, **kwargs):

        mod = importlib.import_module(module)
        if kwargs:
            obj = getattr(mod, object_name)(**kwargs)
        else:
            obj = getattr(mod, object_name)()

        return obj

    def load_components(self):
        logging.info('Loading components')
        self.pipeline = []
        for step in self.STEPS:
            logging.info('Initializing {0}'.format(step))
            try:
                step_object = self.create_object(step, 'Step')
                self.pipeline.append(getattr(step_object, 'run'))
            except:
                logging.warning('Error occured loading {0}'.format(step))
                logging.exception('Error loading pipeline component')

    def run(self, input):
        for component in self.pipeline:
            try:
                component(input)
            except:
                logging.exception('Unable to run component')

