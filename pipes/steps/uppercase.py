import logging

class Step(object):

    def run(self, input):
        logging.info('Converting to uppercase')        
        input['UCASE'] = input['original'].upper()
