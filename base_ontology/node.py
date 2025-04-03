from pydantic import BaseModel, Field


class BaseNode(BaseModel):
    id: str = Field(description="Node için benzersiz bir kimlik")
    reference_text: str = Field(default="", description="Node oluştururken referans alınan metin")
