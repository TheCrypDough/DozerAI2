from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import time # Added for AGUIBaseEvent timestamp

class DozerPrimeQueryInput(BaseModel):
    query: str = Field(..., description="The user's query for Dozer Prime.")
    user_id: str = Field(..., description="The unique identifier of the user making the query (e.g., CEO's user_id).")
    session_id: Optional[str] = Field(None, description="Optional session ID for conversation continuity.")

class RetrievedChunkContext(BaseModel):
    chunk_id: str
    chunk_text: str
    contextual_summary: Optional[str] = None
    document_title: Optional[str] = None
    document_id: Optional[str] = None
    similarity: Optional[float] = Field(None, description="Similarity score from vector search.")

class DozerPrimeRAGOutput(BaseModel):
    llm_response: str = Field(..., description="Dozer Prime's final generated response.")
    retrieved_contexts: List[RetrievedChunkContext] = Field(default_factory=list, description="List of contexts retrieved and used by the LLM.")
    search_query_embedding: Optional[List[float]] = Field(None, description="The vector embedding of the user's query.")
    langfuse_trace_id: Optional[str] = Field(None, description="Trace ID from Langfuse for this interaction.")

class AGUIMessage(BaseModel):
    id: str
    role: str
    content: Optional[str] = None
    name: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None
    tool_call_id: Optional[str] = None

class AGUITool(BaseModel):
    type: str = "function"
    function: Dict[str, Any]

class AGUIRunAgentInput(BaseModel):
    thread_id: str
    run_id: str
    messages: List[AGUIMessage]
    tools: Optional[List[AGUITool]] = Field(default_factory=list)

class AGUIBaseEvent(BaseModel):
    type: str
    thread_id: Optional[str] = None
    run_id: Optional[str] = None
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000))

class AGUIRunStartedEvent(AGUIBaseEvent):
    type: str = "RUN_STARTED"

class AGUIRunFinishedEvent(AGUIBaseEvent):
    type: str = "RUN_FINISHED"

class AGUIRunErrorEvent(AGUIBaseEvent):
    type: str = "RUN_ERROR"
    message: str
    stack_trace: Optional[str] = None

class AGUITextMessageStartEvent(AGUIBaseEvent):
    type: str = "TEXT_MESSAGE_START"
    message_id: str
    role: str = "assistant"

class AGUITextMessageChunkEvent(AGUIBaseEvent):
    type: str = "TEXT_MESSAGE_CHUNK"
    message_id: str
    delta: str

class AGUITextMessageEndEvent(AGUIBaseEvent):
    type: str = "TEXT_MESSAGE_END"
    message_id: str

class AGUIToolCallStartEvent(AGUIBaseEvent):
    type: str = "TOOL_CALL_START"
    tool_call_id: str
    parent_message_id: str
    name: str

class AGUIToolCallEndEvent(AGUIBaseEvent):
    type: str = "TOOL_CALL_END"
    tool_call_id: str
    output: Optional[str] = None 