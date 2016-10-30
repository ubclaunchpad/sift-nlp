# Celery settings

# URL format: transport://user:pass@host:port/vhost
BROKER_URL = 'amqp://sift:sift@localhost:5672/sift'
CELERY_RESULT_BACKEND = 'amqp://sift:sift@localhost:5672/sift'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('sift.jobrunner.jobs',)

# Always JSON for content-type so we can work between Python and Go.
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
