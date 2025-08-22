from fastapi import FastAPI, UploadFile, File
from mangum import Mangum
from s3_utils import upload_file_to_s3

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to WellDesk API running on Lambda!"}

@app.post("/upload_activity/")
async def upload_activity(file: UploadFile = File(...)):
    content = await file.read()
    success = upload_file_to_s3(content, file.filename)
    if success:
        return {"message": "Uploaded to S3", "filename": file.filename}
    else:
        return {"message": "Upload failed"}

handler = Mangum(app)