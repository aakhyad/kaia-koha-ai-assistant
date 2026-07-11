from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_service import ai_service

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = ai_service.chat(request.message)
    return ChatResponse(response=reply)
