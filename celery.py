from __future__ import absolute_import

from celery import Celery

ai_app = Celery('ai_proj',
             broker='amqp://',
             backend='amqp://',
            include=['ai_proj.tasks'])

# Optional configuration, see the application user guide.
ai_app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
        ai_app.start()
