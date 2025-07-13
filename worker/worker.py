import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.tasks import celery

celery.worker_main(["worker", "--loglevel=info"])
