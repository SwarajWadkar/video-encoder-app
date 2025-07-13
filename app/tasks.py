from celery import Celery
from app.utils import encode_video
from app.database import SessionLocal
from app.models import Video

# Create Celery instance
celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def process_video(filename: str):
    input_path = f"/app/uploads/{filename}"
    output_path = f"/app/uploads/encoded_{filename}"

    try:
        encode_video(input_path, output_path)

        db = SessionLocal()
        video = Video(filename=filename)
        db.add(video)
        db.commit()
    except Exception as e:
        print(f"Error processing video: {e}")
    finally:
        db.close()
