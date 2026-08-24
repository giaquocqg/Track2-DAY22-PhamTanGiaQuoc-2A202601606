"""
Patch để fix ragas import errors với langchain mới.
Phải import TRƯỚC khi import ragas.
"""
import sys
from unittest.mock import MagicMock

# Patch ChatVertexAI
try:
    from langchain_community import chat_models
    chat_models.ChatVertexAI = MagicMock()
except ImportError:
    pass

# Patch vertexai module
sys.modules['langchain_community.chat_models.vertexai'] = MagicMock()

# Patch pydantic_v1 nếu thiếu
try:
    from langchain_core import pydantic_v1
except ImportError:
    from langchain_core import pydantic
    sys.modules['langchain_core.pydantic_v1'] = pydantic

print("Ragas patch applied successfully")
