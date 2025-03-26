from pydantic import BaseModel, Field


class BaseNode(BaseModel):
    """
    Represents a basic node in the ontology.

    Attributes:
        id (str): A unique identifier for the node.
        reference_text (str, optional): The reference text used when creating the node.
    """

    id: str = Field(description="Node için benzersiz bir kimlik")
    reference_text: str | None = Field(default=None, description="Node oluştururken referans alınan metin")
