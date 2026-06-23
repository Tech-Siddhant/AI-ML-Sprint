from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Optional
import uvicorn
import asyncio
import pandas as pd # <-- NEW: The Chef is in the building

app = FastAPI(title="Elite Log Aggregator API", version="1.0")

class LogEntry(BaseModel):
    timestamp: str
    ip_address: str
    endpoint: str
    status_code: int
    error_message: Optional[str] = None

# --- PREVIOUS ROUTES ---
@app.get("/")
async def health_check():
    return {"status": "success", "message": "The Log Aggregator API is online and listening."}

@app.post("/ingest-log")
async def ingest_single_log(log: LogEntry):
    return {"status": "success", "message": "Log accepted.", "data": log}

@app.get("/heavy-processing")
async def process_heavy_data():
    await asyncio.sleep(10) 
    return {"status": "success", "message": "Heavy 10-second processing complete."}

# --- TOPIC 4: THE PIPELINE INTEGRATION ---
@app.post("/upload-csv")
async def process_csv(file: UploadFile = File(...)):
    print(f"📥 Waiter: Received file '{file.filename}'. Handing to Pandas Chef...")
    
    # The Waiter hands the internet file directly to the Pandas Engine in-memory!
    df = pd.read_csv(file.file)
    
    # The Chef does rapid analytics
    total_rows = len(df)
    columns = df.columns.tolist()
    
    # Optional: Count how many times each status code appears
    if 'status_code' in df.columns:
        status_counts = df['status_code'].value_counts().to_dict()
    else:
        status_counts = "No 'status_code' column found."

    print("✅ Chef: CSV processed successfully!")
    
    # The Waiter returns the clean analytics JSON back to the internet customer
    return {
        "filename": file.filename,
        "total_rows_processed": total_rows,
        "columns_detected": columns,
        "analytics": status_counts,
        "message": "CSV successfully processed by the Pandas Pipeline."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)