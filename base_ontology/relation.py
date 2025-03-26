from typing import Any

from node import BaseNode
from pydantic import BaseModel, Field


class BaseRelation(BaseModel):
    """
    Represents a basic relation in the ontology.

    Attributes:
        reason (str, optional): The reason for determining this relation.
        attributes (dict): The attributes of the relation.
    """

    source_node: BaseNode
    target_node: BaseNode
    reason: str | None = Field(default=None, description="Bu ilişkiyi çıkarmana karar vermene sahip olan neden")
    attributes: dict[str, Any] = Field(default_factory=lambda: {}, description="İlişkinin özellikleri")
