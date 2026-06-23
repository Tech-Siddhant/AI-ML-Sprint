# 1. Base OS
FROM python:3.11-slim

# 2. Isolated Workspace
WORKDIR /app

# 3. Cache the Blueprint
COPY requirements.txt .

# 4. Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. The Surgical Payload
COPY projects/ ./projects/

# --- NEW: Open the Front Door ---
# This punches a hole in the container so web traffic can get in
EXPOSE 8000

# 6. The Ignition Switch
# We no longer run the Week 1 script. We boot up the Week 3 API server.
CMD ["python", "projects/week03_api.py"]