from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from src.engine.rag_pipeline import LuminaRAGPipeline

app = FastAPI(
    title="Lumina RAG Engine API",
    description="Enterprise Retrieval-Augmented Generation Service",
    version="1.0.0"
)

# Global pipeline instance
pipeline = LuminaRAGPipeline()

class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3

class QueryResponse(BaseModel):
    answer: str
    citations: List[Dict]
    latency: float

@app.get("/")
async def health_check():
    return {"status": "ok", "engine": "Lumina RAG Engine v1.0"}

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Endpoint to process natural language queries across ingested documents.
    """
    try:
        result = pipeline.process_query(request.query)
        return QueryResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)