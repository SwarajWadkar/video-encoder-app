from celery import Celery
from app.utils import encode_video

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def process_video(filename: str):
    input_path = f"/app/uploads/{filename}"
    output_path = f"/app/uploads/encoded_{filename}"
    encode_video(input_path, output_path)
