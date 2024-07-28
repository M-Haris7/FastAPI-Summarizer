from pydantic import BaseModel

class UploadFileResponse(BaseModel):
    session_id: str
    message: str

class SummarizeRequest(BaseModel):
    session_id: str