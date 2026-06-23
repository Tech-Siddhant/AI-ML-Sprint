from fastapi import FastAPI
import uvicorn

# Initialize the API (The Waiter)
app = FastAPI(title="Elite Log Aggregator API", version="1.0")

# Define a "Route" (A specific table the waiter serves)
@app.get("/")
def health_check():
    return {"status": "success", "message": "The Log Aggregator API is online and listening."}

# The Ignition Switch
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)