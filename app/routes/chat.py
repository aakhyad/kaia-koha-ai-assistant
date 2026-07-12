from fastapi import APIRouter, HTTPException
import traceback

from app.schemas.chat import ChatRequest, ChatResponse
from app.ai.service import ai_service

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        reply = await ai_service.chat(request.message)
        return ChatResponse(response=reply)

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
