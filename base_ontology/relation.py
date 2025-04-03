from typing import Any

from pydantic import BaseModel, Field

from base_ontology.node import BaseNode


class BaseRelation(BaseModel):
    source_node: BaseNode
    target_node: BaseNode
    reason: str = Field(default="", description="Bu ilişkiyi çıkarmana karar vermene sahip olan neden")
    attributes: dict[str, Any] = Field(default_factory=lambda: {}, description="İlişkinin özellikleri")
