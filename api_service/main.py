from fastapi import FastAPI, UploadFile, File, HTTPException
from mangum import Mangum
from s3_utils import upload_file_to_s3

app = FastAPI(root_path="/prod")

@app.get("/")
def root():
    return {"message": "Welcome to WellDesk API running on Lambda!"}

@app.post("/upload_activity/")
async def upload_activity(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        contents = await file.read()
        filename = file.filename
        # Now upload to S3
        success = upload_file_to_s3(contents, file.filename)
        if success:
            return {"message": "Uploaded to S3", "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

handler = Mangum(app)