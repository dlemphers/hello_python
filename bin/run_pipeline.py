#!/usr/bin/python

from pipes.lib.pipeline import Pipeline
import logging

if __name__=="__main__":
    logging.basicConfig(level='INFO')
    input = {
        'original': 'Hello Python'
    }
    pipeline = Pipeline()
    logging.info('Input is = {0}'.format(input))
    pipeline.run(input)
    logging.info('Input is now = {0}'.format(input))