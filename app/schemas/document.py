from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    status: str
    upload_timestamp: datetime

    model_config = ConfigDict(from_attributes=True)