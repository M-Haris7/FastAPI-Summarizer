from fastapi import FastAPI, Request, HTTPException, middleware
from routes import router

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException, Request, Header, Depends
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS", "GET"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api", tags=["file operations"])

@app.get("/")
async def root():
    """
    Root endpoint to check the status of the API.

    Returns:
    - JSONResponse indicating the API status
    """
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/api/upload")
async def upload_file(request: Request):
    """
    Upload a text file.

    Parameters:
    - request: Request, the request object containing the file

    Returns:
    - JSONResponse with session ID and message
    """
    form = await request.form()
    print(form)
    file = form.get("file")
    print(file)
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Invalid file type. Only .txt files are allowed.")
    
    content = await file.read()
    text = content.decode("utf-8")
    print(text)
    
    # Generate a unique session ID
    # session_id = str(uuid.uuid4())
    # storage.save_text(session_id, text)
    
    # return UploadFileResponse(session_id=session_id, message="File uploaded successfully.")
    return {"text": text}

