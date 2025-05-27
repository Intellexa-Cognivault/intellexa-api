from fastapi import FastAPI, Depends
from intellexa.db import fetch_records
from .db import init_pool, fetch_records, execute, init_read_pool
import os

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_pool()
    if os.getenv("READ_REPLICA_DSN"):
        await init_read_pool()

@app.on_event("startup")
async def startup():
    # Initialize DB pools
    from intellexa.scripts.init_db import initialize_pools
    await initialize_pools()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    users = await fetch_records(
        "SELECT * FROM users WHERE id = $1", 
        [user_id]
    )
    return users[0] if users else None

@app.post("/users")
async def create_user(name: str, email: str):
    await execute(
        "INSERT INTO users (name, email) VALUES ($1, $2)",
        [name, email]
    )
    return {"status": "created"}

@app.on_event("startup")
async def startup():
    """
    FastAPI startup event. This function is called by FastAPI when the
    application is starting up. It starts the monitoring and initializes
    the database connection pool.
    """
    from .monitoring import start_monitoring
    start_monitoring()
    await init_pool()