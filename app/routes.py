from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
import uuid
from summarize import summarize
from models import UploadFileResponse, SummarizeRequest
from storage import storage

router = APIRouter()

@router.post("/upload", response_model=UploadFileResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a text file.

    Parameters:
    - file: UploadFile, a .txt file to be uploaded

    Returns:
    - JSONResponse with session ID and message
    """
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Invalid file type. Only .txt files are allowed.")
    
    content = await file.read()
    text = content.decode("utf-8")
    print(text)
    
    # Generate a unique session ID
    session_id = str(uuid.uuid4())
    storage.save_text(session_id, text)
    
    return UploadFileResponse(session_id=session_id, message=text)
# async def upload_file(request: Request):
#     """
#     Upload a text file.

#     Parameters:
#     - request: Request, the request object containing the file

#     Returns:
#     - JSONResponse with session ID and message
#     """
#     form = await request.form()
#     print(form)
#     file = form.get("file")
#     print(file)
#     if file.content_type != "text/plain":
#         raise HTTPException(status_code=400, detail="Invalid file type. Only .txt files are allowed.")
    
#     content = await file.read()
#     text = content.decode("utf-8")
#     print(text)
    
#     # Generate a unique session ID
#     # session_id = str(uuid.uuid4())
#     # storage.save_text(session_id, text)
    
#     # return UploadFileResponse(session_id=session_id, message="File uploaded successfully.")
#     return {"text": text}

@router.post("/summarize")
async def summarize_file(request: Request):
    """
    Summarize the content of the uploaded text file.

    Parameters:
    - request: SummarizeRequest, containing the session ID

    Returns:
    - JSONResponse containing the summary of the text
    """
    body = await request.json()
    print(body)
    session_id = body.get("session_id")
    print(session_id)
    text = storage.get_text(session_id)
    print(text)
    if not text:
        raise HTTPException(status_code=404, detail="Session ID not found or text not available.")
    
    summary = summarize(text)
    storage.delete_text(session_id)  # Optionally delete text after summarization
    
    return JSONResponse(content={"summary": summary})
