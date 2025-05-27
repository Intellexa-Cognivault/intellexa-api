# intellexa-api/src/api/health.py
from fastapi import APIRouter
from intellexa.db import check_pool_health

router = APIRouter()

@router.get("/health")
async def health_check():
    db_ok = await check_pool_health()
    return {"database": "ok" if db_ok else "unhealthy"}