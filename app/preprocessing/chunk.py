from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class Chunk:
    """
    Represents a chunk of text ready for embedding.
    """

    chunk_id: str = field(default_factory=lambda: str(uuid4()))

    text: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)