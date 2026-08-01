from pydantic import BaseModel

class ExtractedEntity(BaseModel):
  
    type: str

    original: str

    normalized: str

    confidence: float = 1.0