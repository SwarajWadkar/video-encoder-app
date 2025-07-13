from fastapi import FastAPI, UploadFile, File
from app.tasks import process_video
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Ensure DB tables are created before the app handles requests
    init_db()

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename

    # ✅ Save to shared volume
    with open(f"/app/uploads/{filename}", "wb") as f:
        f.write(contents)

    # ✅ Trigger background Celery task
    process_video.delay(filename)

    return {"message": f"{filename} uploaded and processing started"}
