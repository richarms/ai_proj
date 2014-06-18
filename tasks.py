from __future__ import absolute_import
from ai_proj.celery import ai_app
from ai_proj.celery import *

celery = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@celery.task
def add(x, y):
    print 'adding ' + str(y) + ' and ' + str(y)
    return x + y

@celery.task
def aoflagger(msfile, strategy_file):
    print 'initiate aoflagger here'
    return msfile
