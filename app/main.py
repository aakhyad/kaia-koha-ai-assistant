from fastapi import FastAPI

app = FastAPI(
    title="KAIA - Koha AI Assistant",
    description="AI-powered assistant for the Koha Library Management System",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "application": "KAIA",
        "message": "Welcome to KAIA - Koha AI Assistant",
        "version": "0.1.0"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
