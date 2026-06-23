from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Elite Log Aggregator API", version="1.0")

# --- THE BOUNCER: Pydantic Schema ---
class LogEntry(BaseModel):
    timestamp: str
    ip_address: str
    endpoint: str
    status_code: int # The bouncer forces this to be an integer!
    error_message: Optional[str] = None # Optional means it can be missing

# --- ROUTES ---

@app.get("/")
def health_check():
    return {"status": "success", "message": "The Log Aggregator API is online and listening."}

@app.post("/ingest-log")
def ingest_single_log(log: LogEntry):
    # If the code reaches this line, Pydantic GUARANTEES the data is perfectly formatted.
    return {
        "status": "success", 
        "message": "Log validated by Bouncer and accepted.",
        "data_received": log
    }

# --- IGNITION ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)