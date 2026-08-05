from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class Chunk:
    chunk_id: str = field(default_factory=lambda: str(uuid4()))
    document_id: str = ""
    text: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)