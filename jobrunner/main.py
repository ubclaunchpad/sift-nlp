from celery import Celery

app = Celery()
app.config_from_object('sift.jobrunner.config')

if __name__ == "__main__":
    app.start()
