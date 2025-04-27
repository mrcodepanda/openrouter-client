from typing import Dict, List, Optional, Union, Literal, Any
from pydantic import BaseModel, Field

from .helpers import (
    NonChatChoice, NonStreamingChoice, StreamingChoice, ResponseUsage
)

class OpenRouterResponse(BaseModel):
    pass

class OpenRouterChatCompletionResponse(OpenRouterResponse):
    """Full completion response (non-streaming)"""
    id: str = Field(..., description="Unique identifier for the completion")
    choices: List[NonStreamingChoice] = Field(..., description="List of completion choices")
    created: int = Field(..., description="Unix timestamp of when the completion was created")
    model: str = Field(..., description="Model used for completion")
    object: Literal["chat.completion"] = "chat.completion"
    system_fingerprint: Optional[str] = Field(
        None,
        description="System fingerprint used for content moderation (only present if the provider supports it)"
    )
    usage: ResponseUsage = Field(..., description="Token usage statistics")
    model_owner: Optional[str] = Field(None, description="The owner/provider of the model")


class OpenRouterChatCompletionChunkResponse(OpenRouterResponse):
    """Chunk response for streaming"""
    id: str = Field(..., description="Unique identifier for the completion")
    choices: List[StreamingChoice] = Field(..., description="List of completion choices for this chunk")
    created: int = Field(..., description="Unix timestamp of when the completion was created")
    model: str = Field(..., description="Model used for completion")
    object: Literal["chat.completion.chunk"] = "chat.completion.chunk"
    system_fingerprint: Optional[str] = Field(
        None,
        description="System fingerprint used for content moderation (only present if the provider supports it)"
    )
    usage: Optional[ResponseUsage] = Field(
        None,
        description="Token usage statistics (only in the final chunk for streaming)"
    )
    model_owner: Optional[str] = Field(None, description="The owner/provider of the model")


class OpenRouterNonChatCompletionResponse(OpenRouterResponse):
    """Non-chat completion response"""
    id: str = Field(..., description="Unique identifier for the completion")
    choices: List[NonChatChoice] = Field(..., description="List of completion choices")
    created: int = Field(..., description="Unix timestamp of when the completion was created")
    model: str = Field(..., description="Model used for completion")
    object: Literal["chat.completion"] = "chat.completion"
    system_fingerprint: Optional[str] = Field(
        None,
        description="System fingerprint used for content moderation (only present if the provider supports it)"
    )
    usage: ResponseUsage = Field(..., description="Token usage statistics")
    model_owner: Optional[str] = Field(None, description="The owner/provider of the model")
